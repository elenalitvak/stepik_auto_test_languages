import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Описываем, что ключ language обязателен для запуска данного теста
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default= None, help="Choose language please")

# Описываем, фикстуру, в которой будет открываться версия сайта с учетом языка
@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language") # Получаем значение параметра language из командной строки
    print(f"user language: {user_language}..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) # Запуск браузера с указанным языком
    browser = webdriver.Chrome(options=options)
    yield browser
    print("quit browser..")
    browser.quit()