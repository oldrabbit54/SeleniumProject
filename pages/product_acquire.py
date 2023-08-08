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
        title = title.split(' ')[0]
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
            title = actual_cart_products[i].text.split(' ')[0]
            price = actual_cart_products[i + 1].text
            price = price[:price.find('₽') - 1].strip(' ,.')
            print(title, price)
            assert title in products_in_cart
            assert products_in_cart[title] == price

        print("NAMES & PRICES ARE CORRECT")

    def finish_order(self, first_name, last_name, phone,
                     city, street, building, flat, payment_method, second_phone=None, promocode=None):
        find_and_click_element(By.CSS_SELECTOR, 'input[name="contact-form_firstName"]',
                               self.driver).send_keys(first_name)
        find_and_click_element(By.CSS_SELECTOR, 'input[name="contact-form_lastName"]',
                               self.driver).send_keys(last_name)
        find_and_click_element(By.CSS_SELECTOR, 'input[name="contact-form_phone"]',
                               self.driver).send_keys(phone)
        if second_phone:
            find_and_click_element(By.CSS_SELECTOR, 'input[name="contact-form_additionalPhone"]',
                                   self.driver).send_keys(second_phone)
        print("USER DATA ENTERED")

        find_and_click_element(By.XPATH, '//div[contains(text(), "Доставка")]', self.driver)

        find_and_click_element(By.CSS_SELECTOR, 'input[name="city"]', self.driver).send_keys(city)
        find_and_click_element(By.CSS_SELECTOR, 'input[name="street"]', self.driver).send_keys(street)
        find_and_click_element(By.XPATH, '//*[contains(text(), "Добавить:")]', self.driver)

        find_and_click_element(By.CSS_SELECTOR, 'input[name="courier-delivery-new-address-form_house"]',
                               self.driver).send_keys(building)
        find_and_click_element(By.CSS_SELECTOR, 'input[name = "courier-delivery-new-address-form_flat"]',
                               self.driver).send_keys(flat)

        print("ADDRESS ENTERED")

        find_and_click_element(By.XPATH, f'//span[contains(text(), "{payment_method}")]', self.driver)

        print("PAYMENT METHOD CHOSEN")
        time.sleep(3)
        try:
            self.driver.find_element(By.XPATH, '//span[contains(text(), "Вход")]')
            find_and_click_element(By.CSS_SELECTOR, 'div[data-meta-name="Popup"] button svg', self.driver)
        except:
            pass
        if promocode:
            find_and_click_element(By.CSS_SELECTOR, 'input[name="promoCode"]',
                                   self.driver).send_keys(promocode)
            find_and_click_element(By.XPATH, '//span[contains(text(),"Применить")]',
                                   self.driver)

            print("PROMOCODE ENTERED")

        find_and_click_element(By.CSS_SELECTOR, 'button[data-meta-name="SubmitButton"]',
                               self.driver)

        print("ORDER COMPLETED")

    def assert_success_order(self):
        assert find_and_click_element(By.XPATH,
                                      '//span[contains(text(), "Заказ успешно создан")]', self.driver)










