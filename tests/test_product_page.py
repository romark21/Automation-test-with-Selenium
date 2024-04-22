from config.links import Links
from pages.product_page import ProductPage
from time import sleep


def test_guest_can_add_product_to_basket(browser):
    link = Links.PRODUCT_PAGE
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name_in_basket()
    page.check_product_price_in_basket()

    sleep(5)

