from playwright.sync_api import sync_playwright, Page, expect
import re

with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch()
        page = browser.new_page()
        page.goto("https://robota.ua/ru/zapros/viddalena/ukraine")
        print(expect(page).to_have_title(re.compile('Robota.ua')))
        # print(page.content())
        browser.close()
        print('a')
        print('tqead')