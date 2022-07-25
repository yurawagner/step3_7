from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_see_the_button(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert button != None, 'Not Found'
