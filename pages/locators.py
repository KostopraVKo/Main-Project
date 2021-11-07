from selenium.webdriver.common.by import By
    
class LoginPageLocators:
    LOGIN_URL = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_REPEAT_PASS_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')
    
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
    BUTTON_BASKET = (By.CSS_SELECTOR, '.btn-group > .btn.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_PROD = (By.CSS_SELECTOR, '.col-sm-6.h3')
    BASKET_NOT_PROD_MSG = (By.CSS_SELECTOR, 'div .content_inner > p > a')
    