import pytest

from pages.authorization_manager import AuthorizationManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.run(order=2)
def test_login(test_runner):
    base_url = 'https://www.citilink.ru'
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    driver.maximize_window()
    driver.get(base_url)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[contains(text(), "Я согласен")]'))
        ).click()
    except:
        pass
    p = AuthorizationManager(driver)
    p.login('qwerty@mail.ru', '1234567')