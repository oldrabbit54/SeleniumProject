import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.driver_manager import ChromeDriver

class Filters:
    PRICE = 'PR'
    ORIGINAL = 'OG'

class ProductSelection(ChromeDriver):
    def search_product(self, title):
        search_bar = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, '#__next > div > div.css-1pcsihw.e1s351fz0 > div > div.css-1l8w4nq.es4sr930 > div > div > div.e1r0p2ss0.css-cvzj2n.e1loosed0 > div.css-i9gxme.e1qv3bih0 > form > div > div > label > input'
        )))
        time.sleep(1)
        search_bar.click()
        time.sleep(1)
        search_bar.send_keys(title + Keys.RETURN)


        time.sleep(2)


p = ProductSelection('https://www.citilink.ru/')
p.search_product('айфон 11')


