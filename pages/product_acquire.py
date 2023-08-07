import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.driver_manager import ChromeDriver
from base.functions import find_and_click_element


class ProductAcquire:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):

        find_and_click_element(By.XPATH, '//*[contains(text(), "В корзину")]', self.driver)
        time.sleep(2)
        try:
            find_and_click_element(By.XPATH, '//*[contains(text(), "Перейти в корзину")]', self.driver)
        except NoSuchElementException:
            find_and_click_element(By.XPATH, '//*[contains(text(), "Оформить заказ")]', self.driver)

        print("ADDED TO CART")
        time.sleep(2)

    def buy(self):
        find_and_click_element(By.XPATH, '//button[@title="Перейти к оформлению"]', self.driver)
        print("CREDENTIALS LEFT")

