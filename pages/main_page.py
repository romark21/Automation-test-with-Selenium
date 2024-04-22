from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*self.LOGIN_LINK), 'Login link is not presented'
