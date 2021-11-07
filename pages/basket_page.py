from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_PROD)
        self.is_element_present(*BasketPageLocators.BASKET_NOT_PROD_MSG)