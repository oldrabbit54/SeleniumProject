import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.driver_manager import ChromeDriver




class ProductAcquire:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//*[contains(text(), "В корзину")]')
        )).click()
        time.sleep(2)
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '//*[contains(text(), "Перейти в корзину")]')
            )).click()
        except:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
                (By.XPATH, '//*[contains(text(), "Оформить заказ")]')
            )).click()


        print("ADDED TO CART")
        time.sleep(2)

    def buy(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//button[@title="Перейти к оформлению"]')
        )).click()
        print("CREDENTIALS LEFT")

