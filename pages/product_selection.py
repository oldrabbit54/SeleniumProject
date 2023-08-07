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


class Filters:
    RATING = 'RT'


class ProductSelection(ChromeDriver):
    def apply_filters(self, filters):
        for filter in filters:
            if filter == Filters.RATING:
                try:

                    rating = self.driver.find_element(By.XPATH, f'//input[contains(@name, "rating.{filters[filter]}")]')
                    action = ActionChains(self.driver)
                    action.move_to_element(rating).perform()
                    rating.click()
                    print(f"{filters[filter]} RATING APPLIED")
                except NoSuchElementException:
                    print('NO PRODUCTS WITH SELECTED RATING')



    def search_product(self, title, filters):
        search_bar = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "input[type='search']"
        )))
        time.sleep(1)
        search_bar.click()
        time.sleep(1)
        search_bar.send_keys(title)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        self.apply_filters(filters)
        time.sleep(5)
        try:
            first_match = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div[data-meta-name="SnippetProductVerticalLayout"] > a'))
            )
            action = ActionChains(self.driver)
            action.move_to_element(first_match).perform()
            first_match.click()
            print("ITEM FOUND")
        except NoSuchElementException:
            print("NO ITEM FOUND")



p = ProductSelection('https://www.citilink.ru')
p.search_product('айфон 11', {Filters.RATING : ('3.5')})
p = ProductAcquire(p.driver)
p.add_to_cart()
p.buy()

