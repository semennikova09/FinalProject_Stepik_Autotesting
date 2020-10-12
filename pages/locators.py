from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOKNAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")
    BOOKNAMEINBASKET = (By.CSS_SELECTOR, "#content_inner h1")
    PRICE = (By.CSS_SELECTOR, ".price_color")
    PRICEINBASKET = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
    