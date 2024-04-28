import math
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(self.browser, 10, poll_frequency=1)

    def open(self):
        self.browser.get(self.url)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.url))

    def is_appeared(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, locator):
        try:
            self.wait.until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK))
        login_link.click()

    def should_be_login_link(self):
        assert self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK)), 'Login link is not presented'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
