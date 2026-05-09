from pages.inventoriy_page import InventoryPage
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

def test_add_items_to_cart(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    shopping_cart_badge = page.locator('span[data-test="shopping-cart-badge"]')
    expect(shopping_cart_badge).to_have_text('6')

def test_remove_all_items_from_the_cart(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    shopping_cart_badge = page.locator('span[data-test="shopping-cart-badge"]')
    expect(shopping_cart_badge).to_have_text('6')
    inventory.remove_all_items_from_cart()
    expect(shopping_cart_badge).not_to_be_visible()


def test_remove_3_items_from_the_cart(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    shopping_cart_badge = page.locator('span[data-test="shopping-cart-badge"]')
    expect(shopping_cart_badge).to_have_text('6')
    inventory.remove_three_items_from_cart()
    expect(shopping_cart_badge).to_have_text('3')

def test_open_shopping_cart_page(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    checkout_button = page.get_by_role('button', name='Checkout')
    expect(checkout_button).to_be_visible()

def test_open_hamburger_menu(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_hamburger_menu()
    logout_button = logout_button = page.get_by_role('link', name='Logout')
    expect(logout_button).to_be_visible()


