from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET), "Basket button is not presented"
    
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET)
        button.click()
        
    def should_be_correct_book_name(self):
        name_in_basket = self.browser.find_element(*ProductPageLocators.BOOKNAMEINBASKET).text
        name_in_page = self.browser.find_element(*ProductPageLocators.BOOKNAME).text
        assert name_in_basket==name_in_page, "Books' name is not same"
    
    def should_be_correct_price(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICEINBASKET).text
        price_in_page = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert price_in_page==price_in_basket, "Prices is not same"
   