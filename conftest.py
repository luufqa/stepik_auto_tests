from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language for browser")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()