'''import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_interface_language(browser):
    browser.get(link)
    assert browser.find_element_by_xpath('//button[@type="submit"]')
    time.sleep(30)'''
from .pages.main_page import MainPage 
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()