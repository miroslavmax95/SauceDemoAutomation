from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('standard_user', 'secret_sauce')
    expect(page).to_have_title('Swag Labs')

def test_login_without_username(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('', 'secret_sauce')
    error = page.get_by_text('Epic sadface: Username is required')
    assert error.is_visible()

def test_login_without_password(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('standard_user', '')
    error = page.get_by_text('Epic sadface: Password is required')
    assert error.is_visible()

def test_login_without_credentials(page: Page):
    login_page = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login_page.login('', '')
    error = page.get_by_text('Epic sadface: Username is required')
    assert error.is_visible()

