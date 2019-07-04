import pytest
from selenium import webdriver
#import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_add_to_basket(browser):
    browser.get(link)
    #time.sleep(30)
    basket = browser.find_element_by_css_selector(
        "form button.btn-add-to-basket")
    assert basket.text, "Element not found"
    print(basket.text)
