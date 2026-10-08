#!/usr/bin/env python3
"""Offline slide capture and basic checks. Visual/editorial approval remains manual.
Run with uv run --with playwright --with Pillow python render_review.py deck.html --output fresh-directory
"""
import argparse
import json
from pathlib import Path
from collections import Counter
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('deck', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    deck = args.deck.resolve()
    if not deck.is_file():
        parser.error('Deck does not exist')
    if args.output.exists():
        parser.error('Use a new output directory; existing review evidence will not be overwritten')
    args.output.mkdir(parents=True)
    report = {'deck': str(deck), 'slides': [], 'errors': [], 'blockedRequests': [],
              'visualReview': 'unverified', 'editorialReview': 'unverified', 'userAcceptance': 'pending'}
    with sync_playwright() as playwright:
        chrome = Path('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')
        options = {'headless': True}
        if chrome.exists():
            options['executable_path'] = str(chrome)
        browser = playwright.chromium.launch(**options)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080}, reduced_motion='reduce')

        def block_network(route):
            if route.request.url.startswith(('http:', 'https:')):
                report['blockedRequests'].append(route.request.url)
                route.abort()
            else:
                route.continue_()
        context.route('**/*', block_network)
        page = context.new_page()
        page.on('pageerror', lambda error: report['errors'].append(str(error)))
        page.goto(deck.as_uri())
        page.evaluate('document.fonts.ready')
        if len(page.frames) != 1:
            raise RuntimeError('Frames are not supported by this local renderer')
        slides = page.locator('.slide')
        count = slides.count()
        if not count:
            raise RuntimeError('No .slide elements found')
        jump = page.locator('#jump')
        if count > 1 and not jump.count():
            raise RuntimeError('Provide a #jump select for deterministic navigation, or use browser tools')
        for index in range(count):
            if jump.count():
                jump.select_option(str(index))
            page.wait_for_timeout(80)
            slide = slides.nth(index)
            if 'active' not in (slide.get_attribute('class') or '') and count > 1:
                raise RuntimeError(f'Slide {index + 1} not active after navigation')
            geometry = slide.evaluate('''slide => {
              const bounds=slide.getBoundingClientRect();
              const overflow=[...slide.querySelectorAll('*')].filter(el=>{
                if(el.closest('svg') || el.classList.contains('decorative')) return false;
                const r=el.getBoundingClientRect();
                return r.width>0 && r.height>0 && (r.left<bounds.left-2 || r.top<bounds.top-2 || r.right>bounds.right+2 || r.bottom>bounds.bottom+2);
              }).map(el=>({tag:el.tagName,text:el.textContent.slice(0,100)}));
              const footer=slide.querySelector('.footer, [data-slide-footer]');
              const footerTop=footer ? footer.getBoundingClientRect().top : null;
              const content=[...slide.querySelectorAll('.body *, [data-slide-content] *')].filter(el=>{
                const rect=el.getBoundingClientRect();
                return !el.closest('svg, .decorative, .footer, [data-slide-footer]') && rect.width>0 && rect.height>0;
              });
              const footerCollisions=footerTop===null ? [] : content.filter(el=>el.getBoundingClientRect().bottom>footerTop-8)
                .map(el=>({tag:el.tagName,text:el.textContent.slice(0,100)}));
              const contentBottom=content.length ? Math.max(...content.map(el=>el.getBoundingClientRect().bottom)) : null;
              return {id:slide.id,layout:slide.dataset.layout,purpose:slide.dataset.purpose,overflow,footerCollisions,
                footerCheck:footer && content.length ? 'checked' : 'not-applicable-or-unmarked',
                footerClearance:footerTop!==null && contentBottom!==null ? Math.round(footerTop-contentBottom) : null};
            }''')
            geometry['slide'] = index + 1
            report['slides'].append(geometry)
            slide.screenshot(path=str(args.output / f'slide-{index+1:02}.png'))
        report['assets'] = page.evaluate('({fonts:document.fonts.status, brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).length})')
        if jump.count() and count > 1:
            jump.select_option('0')
            page.locator('body').click(position={'x': 5, 'y': 5})
            page.keyboard.press('ArrowRight')
            report['arrowNavigation'] = page.locator('.slide.active').get_attribute('id') == slides.nth(min(1, count-1)).get_attribute('id')
            if page.locator('#prev').count():
                page.locator('#prev').click()
                report['buttonNavigation'] = page.locator('.slide.active').get_attribute('id') == slides.nth(0).get_attribute('id')
        report['viewportChecks'] = []
        for size in ({'width': 1920, 'height': 1080}, {'width': 1280, 'height': 720}):
            page.set_viewport_size(size)
            for index in range(count):
                if jump.count(): jump.select_option(str(index))
                page.wait_for_timeout(60)
                viewport_check = slides.nth(index).evaluate('''slide => {
                  const bounds=slide.getBoundingClientRect();
                  const controls=document.querySelector('#controls');
                  const bottom=controls ? controls.getBoundingClientRect().top : innerHeight;
                  return {left:bounds.left,top:bounds.top,right:bounds.right,bottom:bounds.bottom,
                    fits:bounds.left>=-2 && bounds.top>=-2 && bounds.right<=innerWidth+2 && bounds.bottom<=bottom+2};
                }''')
                report['viewportChecks'].append({'width': size['width'], 'slide': index+1, **viewport_check})
                if size['width'] == 1280:
                    page.screenshot(path=str(args.output / f'view-1280-{index+1:02}.png'))
        page.set_viewport_size({'width': 390, 'height': 844})
        report['narrowHorizontalOverflow'] = []
        for index in range(count):
            if jump.count(): jump.select_option(str(index))
            page.wait_for_timeout(60)
            if page.evaluate('document.documentElement.scrollWidth > innerWidth + 2'):
                report['narrowHorizontalOverflow'].append(index + 1)
        browser.close()
    layouts = [slide.get('layout') for slide in report['slides']]
    report['layoutCounts'] = dict(Counter(layouts))
    report['repeatedLayoutReview'] = [index+1 for index in range(2,len(layouts)) if layouts[index] and layouts[index]==layouts[index-1]==layouts[index-2]]
    thumbs = []
    for index in range(count):
        with Image.open(args.output / f'slide-{index+1:02}.png') as image:
            thumb = image.convert('RGB')
            thumb.thumbnail((640, 360))
            tile = Image.new('RGB', (660, 400), '#e8eef3')
            tile.paste(thumb, (10, 10))
            ImageDraw.Draw(tile).text((14, 377), f'{index+1:02}  {layouts[index]}', fill='#193247')
            thumbs.append(tile)
    columns = min(3, count)
    sheet = Image.new('RGB', (660*columns,400*((count+columns-1)//columns)), '#e8eef3')
    for index,tile in enumerate(thumbs): sheet.paste(tile, ((index%columns)*660,(index//columns)*400))
    sheet.save(args.output / 'contact-sheet.png')
    report['structuralPass'] = not (report['errors'] or report['blockedRequests'] or report['assets']['brokenImages'] or report['narrowHorizontalOverflow'] or any(not check['fits'] for check in report['viewportChecks']) or any(s['overflow'] or s['footerCollisions'] for s in report['slides']) or report.get('arrowNavigation') is False or report.get('buttonNavigation') is False)
    (args.output / 'review.json').write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report['structuralPass'] else 1)

if __name__ == '__main__':
    main()
