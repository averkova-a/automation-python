import pytest
from selenium import webdriver


# забираем параметр языка
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en, es, fr...")


# открываем окно с заданным языком
@pytest.fixture(scope="function")
def browser(request):
    language_name = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{language_name}/catalogue/coders-at-work_207/"
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()
