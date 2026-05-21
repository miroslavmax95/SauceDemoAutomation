from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):

        ### Login page elements:

        self.page = page
        self.username_field = page.get_by_placeholder('Username')
        self.password_field = page.get_by_placeholder('Password')
        self.login_button = page.get_by_role('button', name='Login')
        self.username_required_error = page.get_by_text('Epic sadface: Username is required')
        self.password_required_error = page.get_by_text('Epic sadface: Password is required')
        self.fake_credentials_error = page.get_by_text('Epic sadface: Username and password do not match any user in this service')
        self.locked_out_user_error = page.get_by_text('Epic sadface: Sorry, this user has been locked out.')


        ### Login method
    def login(self, email: str, password: str):
        self.username_field.fill(email)
        self.password_field.fill(password)
        self.login_button.click()


