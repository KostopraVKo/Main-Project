from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):
        self.should_be_button_add_product_to_basket()
        self.add_product_to_basket()
    
    def test_msg_to_alert(self):
        self.send_message_in_alert()
     
    def should_be_button_add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_CLASS), 'Button is none'
        
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_CLASS).click()
        
    def send_message_in_alert(self):
        self.solve_quiz_and_get_code()
        
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        
    def check_product_name(self, name):
        assert name == self.browser.find_element(*ProductPageLocators.CHECK_PRODUCT).text, 'The name doesn`t not match'
        
    def check_product_price(self, price):
        assert price == self.browser.find_element(*ProductPageLocators.CHECK_PRODUCT_PRICE).text, 'The name doesn`t not match'
        
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), 'Has success message from present'
        
    def test_guest_cant_see_success_message(self): #Only product page
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), 'Page has success message on product page'
        
    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), 'Has success message from disapp'