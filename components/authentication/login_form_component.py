from playwright.sync_api import Page, expect

from elements.input import Input
from pages.base_page import BasePage


class LoginFormComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page,'login-form-email-input', "Email")
        self.password_input = Input(page,'login-form-password-input', 'Password')


    def fill(self, email, password):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def check_visible(self, email, password):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)
