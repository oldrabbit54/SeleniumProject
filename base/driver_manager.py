from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChromeDriver:
    def __init__(self):
        base_url = 'https://www.citilink.ru'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.service = Service()
        self.driver = webdriver.Chrome(options=self.options, service=self.service)
        self.driver.maximize_window()
        self.driver.get(base_url)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[contains(text(), "Я согласен")]'))
            ).click()
        except:
            pass
