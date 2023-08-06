from selenium import webdriver
from selenium.webdriver.chrome.service import Service
class ChromeDriver:
    def __init__(self, base_url):

        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.service = Service()
        self.driver = webdriver.Chrome(options=self.options, service=self.service)
        self.driver.maximize_window()
        self.driver.get(base_url)
        self.driver.implicitly_wait(10)
