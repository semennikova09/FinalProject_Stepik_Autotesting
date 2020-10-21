from .base_page import BasePage
from .locators import GoToBasket
from selenium import webdriver


class BasketPage(BasePage):
    def should_be_message_about_empty_basket(self):
        text_on_page = self.browser.find_element(*GoToBasket.MESSAGE).text
        print(text_on_page)
        assert  text_on_page == "Your basket is empty. Continue shopping", "Message is not correct"
        
    def should_not_be_items(self):
        assert self.is_not_element_present(*GoToBasket.BASKET_ITEMS), "Items are present"


