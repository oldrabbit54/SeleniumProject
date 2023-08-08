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


class ProductSelection(ChromeDriver):
    def apply_filters(self, filters):
        for fltr in filters:
            if fltr == Filters.RATING:
                try:
                    find_and_click_element(By.XPATH,
                                f'//input[contains(@name, "rating.{filters[fltr]}")]', self.driver
                                                    )
                    print(f"{filters[fltr]} RATING APPLIED")
                except NoSuchElementException:
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
        self.apply_filters(filters)
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
p.search_product('айфон 11', {Filters.RATING : '4.5', Filters.AVAILABILITY : [r'#available\.all', r'#available\.instore']})
p = ProductAcquire(p.driver)
p.add_to_cart()
p.buy()
p.assert_order()
p.finish_order('AAAAAA', 'AAAAA', '+79124567788', 'Тюмень', 'Кулибина',
               '1', '1', 'ЮMoney')
p.assert_order()
p.assert_success_order()



