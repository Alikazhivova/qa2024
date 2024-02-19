import re
from playwright.sync_api import Page, expect

email = "asdsdfsg@asda.er"
password = '123456'

def test_login_page(page: Page):
    #открываем страницу
    page.goto("https://demo.opencart.com/admin")
    #ждем 10 секунд
    page.wait_for_load_state('load')
    #ищем элемент "username" по атрибуту placeholde, и дальше применяем метод .fill для заполнения поля текстом "демо"
    page.get_by_placeholder('Username').fill('demo')
    page.get_by_placeholder('Password').fill('demo')
    #ищем элемент по роли "кнопка"
    page.get_by_role('button').click()
    page.wait_for_timeout(3000)
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()


def test_registration_page(page: Page):
    page.goto('http://users.bugred.ru/')
    page.wait_for_load_state('load')
    page.get_by_text('Войти').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("input[name=\"name\"]").fill("Slava")
    page.wait_for_timeout(10000)
    page.locator("input[name=\"email\"]").fill(email)
    page.wait_for_timeout(10000)
    page.locator("tbody").filter(has_text="Имя Email").locator("input[name=\"password\"]").fill(password)
    page.wait_for_timeout(10000)
    page.get_by_role('button', name='Зарегистрироваться').click()


def test_auth_page(page: Page):
    page.goto('http://users.bugred.ru/')
    page.wait_for_load_state('load')
    page.get_by_text('Войти').click()
    page.wait_for_load_state('domcontentloaded')
    page.locator("input[name=\"login\"]").fill(email)
    page.locator("tbody").filter(has_text="Email Пароль Авторизоваться").locator("input[name=\"password\"]").fill(password)
    page.get_by_role('button', name='Авторизоваться').click()
    page.wait_for_load_state('domcontentloaded')
    expect(page.get_by_role("heading", name="Пользователи")).to_be_visible()

    def test_auth_page(page: Page):
        page.goto('http://users.bugred.ru/')
        page.wait_for_load_state('load')
        page.get_by_text('Войти').click()
        page.wait_for_load_state('domcontentloaded')
        page.locator("input[name='login']").fill(Email)
        page.locator("tbody").filter(has_text="Email Пароль Авторизоваться").locator("input[name='password']").fill(password)
        page.get_by_role('button', name='Авторизоваться').click()
        page.wait_for_load_state('domcontentloaded')
        expect(page.get_by_role("heading", name="Пользователи")).to_be_visible()
        page.get_by_placeholder('Введите email или имя').fill('asdsdfsg@asda.er')
        page.get_by_text('Найти').click()
        page.get_by_text('Посмотреть').click()
        text = page.get_by_role('Email',name='asdsdfsg@asda.er')
        expect(text).to_be_visible()