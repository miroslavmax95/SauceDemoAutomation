from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.get_by_placeholder('Username')
        self.password_field = page.get_by_placeholder('Password')
        self.login_button = page.get_by_role('button', name='Login')

    def login(self, email: str, password: str):
        self.username_field.fill(email)
        self.password_field.fill(password)
        self.login_button.click()


