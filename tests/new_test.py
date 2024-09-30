from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def new_test(test_runner):
    base_url = 'https://orioks.miet.ru'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_experimental_option("detach", True)
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(base_url)

