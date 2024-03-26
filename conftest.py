import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Input language!')


@pytest.fixture()
def browser(request):
    user_language = request.config.getoption('language')

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    service = Service(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()

