from selenium.webdriver.common.by import By

#class MainPageLocators:
    
    
class LoginPageLocators:
    LOGIN_URL = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    
class ProductPageLocators:
    BUTTON_CLASS = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    CHECK_PRODUCT = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success > .alertinner > strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.price_color')
    CHECK_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info > .alertinner > p > strong')
    SUCCESS_MSG = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-success > .alertinner')
    
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INV = (By.CSS_SELECTOR, '#login_link_inv')
    