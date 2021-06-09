import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: Chrome")
    parser.addoption('--language', action='store', default=None, help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    # Выбор браузера (только Хром по условию задачи):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name != "chrome":  # Ошибка, если Хром не выбран
        raise pytest.UsageError("--Должен быть выбран Chrome")

    # выбор языка:
    chosen_language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': chosen_language})

    if chosen_language:
        print("\nstart chrome browser for test, language =", chosen_language)
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be chosen")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
