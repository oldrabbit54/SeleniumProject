import pytest

from pages.product_acquire import ProductAcquire
from pages.product_selection import ProductSelection, Filters
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_buy_product(test_runner):
    base_url = 'https://www.citilink.ru'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_experimental_option("detach", True)
    service = Service()

    driver = webdriver.Chrome(options=options, service=service)
    #driver.maximize_window()
    driver.get(base_url)

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "Я согласен")]'))
        ).click()
    except:
        pass

    p = ProductSelection(driver)
    p.search_product('айфон 13',
                     {Filters.RATING: '4.5', Filters.AVAILABILITY: [r'#available\.all', r'#available\.instore']})
    pa = ProductAcquire(driver)
    pa.add_to_cart()
    pa.buy()
    pa.assert_order()
    pa.finish_order('AAAAAA', 'AAAAA', '+79124567788', 'Тюмень', 'Ленина',
                   '1', '1', 'ЮMoney', "lol@lol.com")
