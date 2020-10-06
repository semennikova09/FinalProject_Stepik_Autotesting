from .pages.login_page import LoginPage
from .pages.locators import LoginPageLocators

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    browser.get(link)
    page = LoginPage(browser, link)
    page.open()
    #page.should_be_login_link()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()
    