from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.wait.until(EC.url_contains('login')), \
            'Login url is not correct!'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.wait.until(EC.visibility_of_element_located(self.LOGIN_FORM)), \
            'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.wait.until(EC.visibility_of_element_located(self.REGISTER_FORM)), \
            'Registration form is not presented'
