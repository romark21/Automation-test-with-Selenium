from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.col-sm-6 h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME_ADDED_TO_BASKET = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    PRODUCT_PRICE_ADDED_TO_BASKET = (By.XPATH, "//div[@id='messages']/div[3]//strong")

    def add_to_basket(self):
        add_to_basket_button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD_TO_BASKET))
        add_to_basket_button.click()

    def check_product_name_in_basket(self):
        product_name = self.wait.until(EC.presence_of_element_located(self.PRODUCT_NAME)).text
        product_name_added_to_basket = self.wait.until(
            EC.presence_of_element_located(self.PRODUCT_NAME_ADDED_TO_BASKET)).text
        # print(product_name)
        # print(product_name_added_to_basket)
        assert product_name == product_name_added_to_basket, \
            (f'Product name: "{product_name}"'
             f'and name of product in the cart: '
             f'"{product_name_added_to_basket}"'
             f'is different!')

    def check_product_price_in_basket(self):
        product_price = self.wait.until(EC.presence_of_element_located(self.PRODUCT_PRICE)).text
        product_price_added_to_basket = self.wait.until(
            EC.presence_of_element_located(self.PRODUCT_PRICE_ADDED_TO_BASKET)).text
        # print(product_price)
        # print(product_price_added_to_basket)
        assert product_price == product_price_added_to_basket, \
            (f'Product price: "{product_price}"'
             f'and price of product in the cart: '
             f'"{product_price_added_to_basket}"'
             f'is different!')

    def should_not_be_success_message(self):
        assert self.is_appeared(self.PRODUCT_NAME_ADDED_TO_BASKET), \
            'Success message is presented, but should not be'

    def should_be_success_message(self):
        assert self.is_disappeared(self.PRODUCT_NAME_ADDED_TO_BASKET), \
            'Success message is not presented, but should be'
