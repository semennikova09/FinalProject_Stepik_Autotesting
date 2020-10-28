from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest
from .pages.locators import LoginPageLocators


    
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser_language):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser_language, link)
    page.open()
    page.go_to_basket_page()
    page.should_not_be_items()
    page.should_be_message_about_empty_basket()
    

