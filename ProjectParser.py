from playwright.sync_api import sync_playwright
import re

# k = []
# i = 0
# match = re.findall('Викладач', text)
# print(match)
# print(re.search('Викладач', text).start())
with open('a.txt', 'r') as a:
    email = a.readline()
    password = a.readline()
with sync_playwright() as p:
    for browser_type in [p.chromium]:
        browser = browser_type.launch(headless=False) #тіло браузера
        page = browser.new_page() #тіло сторінки
        page.goto("https://robota.ua/auth/login") #перехід на сторінку
        page.get_by_label('Email або номер телефону').fill(email) # вводимо емейл
        page.get_by_label('Введіть пароль').fill(password) #вводимо пароль
        # Кнопка увійти
        page.locator('xpath=/html/body/app-root/div/alliance-login-page/div/alliance-login-desktop/div/lib-login-form/div/div/santa-button-spinner/div/santa-button/button').click()
        page.get_by_label('Пошук за професією, компанією, навичкою').fill('Викладач python') #заповнюємо поле інпута пошуком по підпису(label) цього інпута
        # кнопка пошук
        page.locator('xpath=//*[@id="cdk-overlay-3"]/div/alliance-jobseeker-default-header/div/div/alliance-jobseeker-search/section/santa-button/button').click()
        page.wait_for_timeout(8000)
        x = 1
        vacan = page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancies-root-page/div/alliance-jobseeker-desktop-vacancies-page/main/section/div/div/lib-desktop-top-info/div/div/div').text_content()
        num_of_vacan = lambda vacan: ''.join(x for x in vacan if x.isdigit()) #функця для отримання цифр з стрічки
        # # ДОДАТИ СЮДИ 'https://robota.ua/'. Отримуємо посилання на роботу
        # href=page.locator(f'xpath=/html/body/app-root/div/alliance-jobseeker-vacancies-root-page/div/alliance-jobseeker-desktop-vacancies-page/main/section/div/alliance-jobseeker-desktop-vacancies-list/div/div[{x}]/alliance-vacancy-card-desktop/a').get_attribute('href')
        # page.locator(
        #     f'xpath=/html/body/app-root/div/alliance-jobseeker-vacancies-root-page/div/alliance-jobseeker-desktop-vacancies-page/main/section/div/alliance-jobseeker-desktop-vacancies-list/div/div[{x}]/alliance-vacancy-card-desktop/a/div'
        # ).click() # натискаємо на потрібну вакансію
        # distant = page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[1]/div/div[4]/alliance-vac-list-status-label/div').inner_text()
        # job_title = page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[1]/div/h1').inner_text()
        # salary = page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[1]/div/div[5]').inner_text()
        # date = page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[2]/santa-tooltip/div/div[1]/span').inner_text()
        # description = page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[3]').inner_text()
        # # кнопка повернутися
        # page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/lib-top-bar/div/santa-button/button').click()
        # print(href, '\n',distant, job_title, salary, date, description)
        # # aa
        try:
            while x <= int(num_of_vacan(vacan)):
                try:
                    href = page.locator(
                        f'xpath=/html/body/app-root/div/alliance-jobseeker-vacancies-root-page/div/alliance-jobseeker-desktop-vacancies-page/main/section/div/alliance-jobseeker-desktop-vacancies-list/div/div[{x}]/alliance-vacancy-card-desktop/a').get_attribute(
                        'href')
                    page.locator(
                        f'xpath=/html/body/app-root/div/alliance-jobseeker-vacancies-root-page/div/alliance-jobseeker-desktop-vacancies-page/main/section/div/alliance-jobseeker-desktop-vacancies-list/div/div[{x}]/alliance-vacancy-card-desktop/a/div'
                    ).click()  # натискаємо на потрібну вакансію
                    distant = page.locator(
                        'xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[1]/div/div[4]/alliance-vac-list-status-label/div').inner_text()
                    job_title = page.locator(
                        'xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[1]/div/h1').inner_text()
                    salary = page.locator(
                        'xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[1]/div/div[5]').inner_text()
                    date = page.locator(
                        'xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[2]/santa-tooltip/div/div[1]/span').inner_text()
                    description = page.locator(
                        'xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div/lib-content/div[3]').inner_text()
                    # кнопка повернутися
                    page.locator(
                        'xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/lib-top-bar/div/santa-button/button').click()
                    x += 1
                except Exception as e:
                    print(f"Помилка на елементі {x}: {e}")
                    break
        except IndexError:
            pass
        # print(page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancy-page/div/alliance-root-page-desktop/article/div[1]/div/div[1]/div/div').inner_text())

        # print(page.locator('xpath=/html/body/app-root/div/alliance-jobseeker-vacancies-root-page/div/alliance-jobseeker-desktop-vacancies-page/main/section/div/alliance-jobseeker-desktop-vacancies-list/div/div[2]/alliance-vacancy-card-desktop/a/div').inner_text())
        page.wait_for_timeout(30000)
        # cont = str(page.content())
        # print(cont)
        # with open('parsed.txt', 'w', encoding='utf-8') as f:
        #     f.write(cont)

        # print(expect(page).to_have_title(re.compile('Robota.ua')))
        browser.close()
