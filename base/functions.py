import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_and_click_element(by: str, locator: str, driver):
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(
                (by, locator))
            )
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    element.click()
    time.sleep(1)
    return element


def go_to_main_page(driver, base_url):
    driver.get(base_url)