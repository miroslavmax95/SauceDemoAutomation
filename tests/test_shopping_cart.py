from pages.checkout_page_step_one import CheckoutPageOne
from pages.inventoriy_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import Page, expect

def test_add_items_to_cart(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    expect(inventory.shopping_cart_badge).to_have_text('6')

def test_remove_all_items_from_the_cart(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    expect(inventory.shopping_cart_badge).to_have_text('6')
    inventory.remove_all_items_from_cart()
    expect(inventory.shopping_cart_badge).not_to_be_visible()


def test_remove_3_items_from_the_cart(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    expect(inventory.shopping_cart_badge).to_have_text('6')
    inventory.remove_three_items_from_cart()
    expect(inventory.shopping_cart_badge).to_have_text('3')

def test_open_shopping_cart_page(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    cart_page = CartPage(page)
    expect(cart_page.checkout_button).to_be_visible()

def test_remove_all_items_from_the_cart_page(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart_page = CartPage(page)
    cart_page.remove_all_from_cart_page()
    expect(inventory.shopping_cart_badge).to_be_hidden()

def test_remove_two_items_from_the_cart_page(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart_page = CartPage(page)
    cart_page.remove_two_items_from_cart_page()
    expect(inventory.shopping_cart_badge).to_have_text('4')

def test_continue_shopping_button(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart_page = CartPage(page)
    cart_page.continue_shopping()
    expect(inventory.title).to_have_text('Products')








