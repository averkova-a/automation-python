from .base_page import BasePage
from .locators import  LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "It's wrong url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There's no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM), "There's no registr form"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON).click()


