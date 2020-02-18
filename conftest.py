import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


# забираем параметр языка
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, es, fr...")


@pytest.fixture(scope="function")
def browser(request):
    # Передаём язык из cmd
    user_language = request.config.getoption('language')
    # Инициализируются опции браузера
    options = Options()
    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    time.sleep(10)
    browser.quit()
