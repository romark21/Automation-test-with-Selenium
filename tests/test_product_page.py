import pytest
from config.links import Links
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from time import sleep


LINK = f'{Links.HOST}/catalogue/coders-at-work_207/'


@pytest.mark.parametrize('link',
                         [f'{Links.PROMO_LINK_TEMPLATE}offer0',
                          f'{Links.PROMO_LINK_TEMPLATE}offer1',
                          f'{Links.PROMO_LINK_TEMPLATE}offer2',
                          f'{Links.PROMO_LINK_TEMPLATE}offer3',
                          f'{Links.PROMO_LINK_TEMPLATE}offer4',
                          f'{Links.PROMO_LINK_TEMPLATE}offer5',
                          f'{Links.PROMO_LINK_TEMPLATE}offer6',
                          pytest.param(f'{Links.PROMO_LINK_TEMPLATE}offer7',
                                       marks=pytest.mark.xfail(reason='bug in basket')),
                          f'{Links.PROMO_LINK_TEMPLATE}offer8',
                          f'{Links.PROMO_LINK_TEMPLATE}offer9'])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name_in_basket()
    page.check_product_price_in_basket()


@pytest.mark.xfail
@pytest.mark.Message_test
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.Message_test
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.Message_test
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_to_basket()
    page.should_be_success_message()


@pytest.mark.Login_link
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.Login_link
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    sleep(2)
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()

