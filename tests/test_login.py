from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('standard_user', 'secret_sauce')
    expect(page).to_have_title('Swag Labs')
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')

def test_login_without_username(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('', 'secret_sauce')
    expect(login_page.username_required_error).to_be_visible()

def test_login_without_password(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('standard_user', '')
    expect(login_page.password_required_error).to_be_visible()

def test_login_without_credentials(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('', '')
    expect(login_page.username_required_error).to_be_visible()

def test_fake_credentials(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('notsupporteduser', '123pass')
    expect(login_page.fake_credentials_error).to_be_visible()

def test_login_with_locked_out_user(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('locked_out_user', 'secret_sauce')
    expect(login_page.locked_out_user_error).to_be_visible()