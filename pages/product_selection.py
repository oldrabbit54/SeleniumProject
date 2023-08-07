import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.driver_manager import ChromeDriver
from pages.product_acquire import ProductAcquire
from base.functions import find_and_click_element, go_to_main_page
from pages.authorization_manager import AuthorizationManager
class Filters:
    RATING = 'RT'


class ProductSelection(ChromeDriver):
    def apply_filters(self, filters):
        for fltr in filters:
            if fltr == Filters.RATING:
                try:
                    rating = find_and_click_element(By.XPATH,
                                f'//input[contains(@name, "rating.{filters[fltr]}")]', self.driver)
                    print(f"{filters[fltr]} RATING APPLIED")
                except NoSuchElementException:
                    print('NO PRODUCTS WITH SELECTED RATING')



    def search_product(self, title, filters = None):
        search_bar = find_and_click_element(By.CSS_SELECTOR, "input[type='search']", self.driver)
        time.sleep(1)
        search_bar.send_keys(title)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        #self.apply_filters(filters)
        time.sleep(5)
        try:
            find_and_click_element(By.CSS_SELECTOR, 'div[data-meta-name="ProductVerticalSnippet"]:first-child', self.driver)
            print("ITEM FOUND")
        except NoSuchElementException:
            print("NO ITEM FOUND")




base_url = 'https://www.citilink.ru'
p = ProductSelection('https://www.citilink.ru')
# p = AuthorizationManager(p.driver)
# p.login('qwerty@mail.ru', '1234567')
p.search_product('ear pods')
p = ProductAcquire(p.driver)
p.add_to_cart()
p.buy()
p.assert_order()



