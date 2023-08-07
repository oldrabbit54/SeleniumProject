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


products_in_cart: dict[str: str] = {}
class ProductAcquire:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[data-meta-name="ProductHeaderLayout__title"] > h1')
        )).text
        price = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[data-meta-name="PriceBlock__price"] span[data-meta-is-total="notTotal"] > span:first-child')
        )).text
        products_in_cart[title] = price.strip('., ')
        print(title, price)
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


    def assert_order(self):
        actual_cart_products = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-meta-name="Aside__wrapper"] div[data-meta-name="AsideOrder__item"] > span')
        for i in range(0, len(actual_cart_products) - 1, 2):
            title = actual_cart_products[i].text
            price = actual_cart_products[i + 1].text
            price = price[:price.find('₽') - 1]
            assert title in products_in_cart
            assert products_in_cart[title] == price

        print("NAMES & PRICES ARE CORRECT")