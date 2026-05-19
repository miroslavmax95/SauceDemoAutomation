from pages.inventoriy_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page_step_one import CheckoutPageOne
from pages.checkout_page_step_two import CheckoutPageTwo
from pages.checkout_complete_page import CheckoutComplete
from playwright.sync_api import Page, expect

def test_open_checkout_step_one(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    expect(page).to_have_url('https://www.saucedemo.com/checkout-step-one.html')

def test_checkout_page_one_cancel_button(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    expect(page).to_have_url('https://www.saucedemo.com/checkout-step-one.html')
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.go_back_to_cart_via_cancel_button()
    expect(page).to_have_url('https://www.saucedemo.com/cart.html')

def test_proceed_to_checkout_step_two(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.fill_all_data('Test', 'User', '15300')
    checkout_step_one.proceed_to_step_two_via_continue_button()
    expect(page).to_have_url('https://www.saucedemo.com/checkout-step-two.html')

def test_proceed_to_checkout_step_two_without_user_data(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.proceed_to_step_two_via_continue_button()
    expect(checkout_step_one.first_name_error).to_be_visible()

def test_proceed_to_checkout_step_two_without_firstname(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.fill_in_last_name('Test')
    checkout_step_one.fill_in_zip_number('15300')
    checkout_step_one.proceed_to_step_two_via_continue_button()
    expect(checkout_step_one.first_name_error).to_be_visible()

def test_proceed_to_checkout_step_two_without_lastname(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.fill_in_first_name('TestFirstName')
    checkout_step_one.fill_in_zip_number('15300')
    checkout_step_one.proceed_to_step_two_via_continue_button()
    expect(checkout_step_one.last_name_error).to_be_visible()

def test_proceed_to_checkout_step_two_without_zip_number(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.fill_in_first_name('Test')
    checkout_step_one.fill_in_last_name('User')
    checkout_step_one.proceed_to_step_two_via_continue_button()
    expect(checkout_step_one.zip_number_error).to_be_visible()

def test_full_checkout_flow_all_items_added(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_all_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.fill_all_data('Test', 'User', '15300')
    checkout_step_one.proceed_to_step_two_via_continue_button()
    expect(page).to_have_url('https://www.saucedemo.com/checkout-step-two.html')
    step_two = CheckoutPageTwo(page)
    expect(step_two.total_value).to_have_text('Total: $140.34')
    expect(step_two.shipping_information).to_have_text('Free Pony Express Delivery!')
    step_two.finish_checkout()
    checkout_completed = CheckoutComplete(page)
    expect(checkout_completed.checkout_complete_message).to_be_visible()


def test_full_checkout_flow_with_3_items_added(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_three_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.fill_all_data('Arthas', 'Menethil', '13202')
    checkout_step_one.proceed_to_step_two_via_continue_button()
    step_two_page = CheckoutPageTwo(page)
    expect(step_two_page.total_value).to_have_text('Total: $82.05')
    expect(step_two_page.payment_information).to_have_text('SauceCard #31337')
    step_two_page.finish_checkout()
    checkout_completed = CheckoutComplete(page)
    expect(page).to_have_url('https://www.saucedemo.com/checkout-complete.html')
    expect(checkout_completed.checkout_complete_message).to_be_visible()



def test_back_home_button_when_flow_is_completed(logged_in_page: Page):
    page = logged_in_page
    inventory = InventoryPage(page)
    inventory.add_three_items_to_the_cart()
    inventory.open_shopping_cart_page()
    cart = CartPage(page)
    cart.go_to_the_checkout_page()
    checkout_step_one = CheckoutPageOne(page)
    checkout_step_one.fill_all_data('Arthas', 'Menethil', '13202')
    checkout_step_one.proceed_to_step_two_via_continue_button()
    step_two_page = CheckoutPageTwo(page)
    expect(step_two_page.total_value).to_have_text('Total: $82.05')
    expect(step_two_page.payment_information).to_have_text('SauceCard #31337')
    step_two_page.finish_checkout()
    checkout_completed = CheckoutComplete(page)
    checkout_completed.go_back_home_after_checkout()
    expect(page).to_have_url('https://www.saucedemo.com/inventory.html')









