import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # опция: запуск браузера в фоне
chrome_options.add_argument('--ignore-certificate-errors')  # опция: игнор ошибок сертификатов
# chrome_options.add_argument('--window-size=1920,1080')  # опция: размер экрана браузера
chrome_options.add_argument('--disable-cache')  # опция: отключение кеширования
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # отключение WebDriver-мода
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0")  # Изменение User-agent


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.get("https://stellarburgers.nomoreparties.site/")
    yield chrome_driver
    chrome_driver.quit()
