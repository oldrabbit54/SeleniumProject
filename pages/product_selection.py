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
    AVAILABILITY = 'AVLB'


class ProductSelection:
    def __init__(self, driver):
        self.driver = driver
    def apply_filters(self, filters):
        for fltr in filters:
            if fltr == Filters.RATING:
                try:
                    find_and_click_element(By.XPATH,
                                f'//input[contains(@name, "rating.{filters[fltr]}")]', self.driver
                                                    )
                    print(f"{filters[fltr]} RATING APPLIED")
                except:
                    print('NO PRODUCTS WITH SELECTED RATING')
            if fltr == Filters.AVAILABILITY:
                for available_status in filters[fltr]:
                    try:
                        print(available_status)
                        find_and_click_element(By.CSS_SELECTOR, available_status, self.driver)
                        print("AVAILABILITY OPTION CHOSEN")
                    except:
                        print("CANNOT CHOOSE AVAILABILITY OPTION")



    def search_product(self, title, filters = None):
        search_bar = find_and_click_element(By.CSS_SELECTOR, "input[type='search']", self.driver)
        time.sleep(1)
        search_bar.send_keys(title)
        search_bar.send_keys(Keys.ENTER)
        print("SEARCHING PRODUCT")

        time.sleep(2)
        if filters:
            self.apply_filters(filters)
        time.sleep(5)
        try:
            find_and_click_element(By.CSS_SELECTOR, 'div[data-meta-name="ProductVerticalSnippet"]:first-child', self.driver)
            print("ITEM FOUND")
        except:
            print("NO ITEM FOUND")






