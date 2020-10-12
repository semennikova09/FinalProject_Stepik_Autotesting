from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login Url is not presented"
        assert self.url=="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login Form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register Form is not presented"
        
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
