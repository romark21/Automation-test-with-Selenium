from pages.main_page import MainPage
from pages.login_page import LoginPage
from config.links import Links


def test_guest_can_go_to_login_page(browser):
    link = Links.MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)  # Переход с главной страницы на страницу логина
    login_page.should_be_login_page()  # Переходим на страницу логина и запускам функцию should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = Links.MAIN_PAGE
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_be_login_page(browser):
    link = Links.LOGIN_PAGE
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

