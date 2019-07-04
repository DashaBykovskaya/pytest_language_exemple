import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language ar de el es fr it nl pl ro ru sk uk en-gb")
        
@pytest.fixture(scope="function")
def browser(request):
    languages = "ar de el es fr it nl pl ro ru sk uk en-gb"
    language = request.config.getoption("language")
    if (language + " ") in languages:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nlanguage {} not supported :(\ntry: ar de el es fr it nl pl ro ru sk uk en-gb".format(language))
        pytest.fail("Wrong Language")
    yield browser
    print("\nquit browser..")
    browser.quit()
