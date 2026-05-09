import pytest
from playwright.sync_api import Page, sync_playwright
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope='function')
def logged_in_page(page: Page):
    login = LoginPage(page)
    page.goto('https://www.saucedemo.com')
    login.login('standard_user', 'secret_sauce')
    return page
