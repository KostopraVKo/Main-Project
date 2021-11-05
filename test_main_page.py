import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_interface_language(browser):
    browser.get(link)
    assert browser.find_element_by_xpath('//button[@type="submit"]')
    time.sleep(30)



#def test_guest_can_go_to_login_page(browser):
 #   link = "http://selenium1py.pythonanywhere.com/"
  #  browser.get(link)
   # login_link = browser.find_element_by_css_selector("#login_link")
    #login_link.click()