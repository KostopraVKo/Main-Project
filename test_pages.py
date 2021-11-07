from .pages.product_page import ProductPage
import pytest
import time

def test_cant_see_success_msg(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_cant_see_success_message()
    
def test_cant_see_success_msg_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.test_guest_cant_see_success_message_after_adding_product_to_basket()

def test_cant_see_disapp_msg(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.guest_can_add_product_to_basket()
    page.test_message_disappeared_after_adding_product_to_basket()
    