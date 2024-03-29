import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_add_to_basket_is_present(browser):
    browser.get(link)
    #time.sleep(30)
    buttons = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert len(buttons) > 0,'Кнопка добавления товара в корзину отсутствует!'
    
    





