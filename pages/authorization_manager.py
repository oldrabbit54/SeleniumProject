import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.driver_manager import ChromeDriver
from base.functions import find_and_click_element, go_to_main_page


class AuthorizationManager:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        #div[data-meta-name="UserButtonContainer"] > div
        go_to_main_page(self.driver, 'https://www.citilink.ru')
        find_and_click_element(By.CSS_SELECTOR, 'div[data-meta-name="UserButtonContainer"] > div', self.driver)
        find_and_click_element(By.XPATH, '//*[contains(text(), "Вход")]', self.driver)

        username_field = find_and_click_element(By.CSS_SELECTOR, 'input[name="login"]', self.driver)
        username_field.send_keys(username)

        password_field = find_and_click_element(By.CSS_SELECTOR, 'input[name="pass"]', self.driver)
        password_field.send_keys(password)

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, '//form/div/button/span[contains(text(), "Войти")]'))
        ).click()
        #find_and_click_element(By.XPATH, '//form/div/button/span[contains(text(), "Войти")]', self.driver)

