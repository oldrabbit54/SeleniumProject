from re import search

import pytest
from selenium.common import NoSuchElementException

from base.functions import find_and_click_element, find_element
from pages.authorization_manager import AuthorizationManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login(test_runner):
    base_url = 'https://orioks.miet.ru'
    options = webdriver.ChromeOptions()
    options.add_argument("--start-fullscreen")
    options.add_experimental_option("detach", True)
    service = Service()
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(base_url)

    find_and_click_element(By.CSS_SELECTOR, "#loginform-login",
                           driver).send_keys("")

    find_and_click_element(By.CSS_SELECTOR, "#loginform-password",
                           driver).send_keys("")


    find_and_click_element(By.CSS_SELECTOR, "#loginbut",
                           driver)





    my_name = find_element(By.CSS_SELECTOR, "#w4 > li:nth-child(3) > a",
                                     driver).text

    assert "военушкин" in my_name.lower()