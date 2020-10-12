from .pages.login_page import LoginPage
#from .pages.locators import LoginPageLocators

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    #page.should_be_login_link()
    #page.should_be_login_url()
    #page.should_be_login_form()
    #page.should_be_register_form()
    