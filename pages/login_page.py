from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, "URL is not correct"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert self.is_element_present(login_form), "Login form is not present"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert self.is_element_present(register_form), "Register form is not present"