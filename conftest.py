import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose locale language")


@pytest.fixture()
def browser(request):
    browser_name_value = request.config.getoption("--browser_name")
    if browser_name_value == "chrome":
        languages = "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb "
        language = request.config.getoption("language")
        if (language + " ") in languages:
            print("\nstart chrome browser for test..")
            options = Options()
            options.add_experimental_option(
                'prefs', {'intl.accept_languages': language})
            browser = webdriver.Chrome(options=options)
        else:
            print(
                "\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk "
                "zh-hans en-gb".format(
                    language))
            pytest.fail("Wrong Language")
    elif browser_name_value == "firefox":
        languages = "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb "
        language = request.config.getoption("language")
        if (language + " ") in languages:
            print("\nstart firefox browser for test..")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            print(
                "\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk "
                "zh-hans en-gb".format(
                    language))
            pytest.fail("Wrong Language")
    yield browser
    print("\nquit browser..")
    browser.quit()
