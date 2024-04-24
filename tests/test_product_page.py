import pytest
from config.links import Links
from pages.product_page import ProductPage
from time import sleep


@pytest.mark.parametrize('link',
                         [f'{Links.PROMO_LINK_TAMPLATE}offer0',
                          f'{Links.PROMO_LINK_TAMPLATE}offer1',
                          f'{Links.PROMO_LINK_TAMPLATE}offer2',
                          f'{Links.PROMO_LINK_TAMPLATE}offer3',
                          f'{Links.PROMO_LINK_TAMPLATE}offer4',
                          f'{Links.PROMO_LINK_TAMPLATE}offer5',
                          f'{Links.PROMO_LINK_TAMPLATE}offer6',
                          pytest.param(f'{Links.PROMO_LINK_TAMPLATE}offer7',
                                       marks=pytest.mark.xfail(reason='bug in basket')),
                          f'{Links.PROMO_LINK_TAMPLATE}offer8',
                          f'{Links.PROMO_LINK_TAMPLATE}offer9'])
def test_guest_can_add_product_to_basket(browser, link):
    # link = Links.PRODUCT_PAGE_2
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product_name_in_basket()
    page.check_product_price_in_basket()
    sleep(2)
