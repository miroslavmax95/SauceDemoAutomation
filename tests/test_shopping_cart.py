from pages.inventoriy_page import InventoryPage
from pages.cart_page import CartPage
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

# def test_open_hamburger_menu(logged_in_page: Page):
#     page = logged_in_page
#     inventory = InventoryPage(page)
#     inventory.open_hamburger_menu()
#     logout_button = logout_button = page.get_by_role('link', name='Logout')
#     expect(logout_button).to_be_visible()

def test_remove_all_items_from_the_cart_page(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart_page = CartPage(page)
    cart_page.remove_all_from_cart_page()
    shopping_cart_badge = page.locator('span[data-test="shopping-cart-badge"]')
    assert shopping_cart_badge.is_hidden()

def test_remove_two_items_from_the_cart_page(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart_page = CartPage(page)
    cart_page.remove_two_items_from_cart_page()
    shopping_cart_badge = page.locator('span[data-test="shopping-cart-badge"]')
    expect(shopping_cart_badge).to_have_text('4')

def test_continue_shopping_button(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart_page = CartPage(page)
    cart_page.continue_shopping()
    title = page.locator('span[data-test="title"]')
    expect(title).to_have_text('Products')

def test_go_to_checkout_page(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart_page = CartPage(page)
    cart_page.go_to_the_checkout_page()
    checkout_page_title = page.locator('span[data-test="title"]')
    expect(checkout_page_title).to_have_text('Checkout: Your Information')




