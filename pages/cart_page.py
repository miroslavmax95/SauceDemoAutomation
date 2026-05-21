from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):

        ### Cart page buttons:
        self.page = page
        self.continue_shopping_button = page.get_by_role('button', name='Continue Shopping')
        self.checkout_button = page.get_by_role('button' , name='Checkout')

        ### Cart page remove item buttons, per item
        self.remove_backpack_from_cart_button = page.locator('button[data-test="remove-sauce-labs-backpack"]')
        self.remove_bikelight_from_cart_button = page.locator('button[data-test="remove-sauce-labs-bike-light"]')
        self.remove_tshirt_from_cart_button = page.locator('button[data-test="remove-sauce-labs-bolt-t-shirt"]')
        self.remove_jacket_from_cart_button = page.locator('button[data-test="remove-sauce-labs-fleece-jacket"]')
        self.remove_onesie_from_cart_button = page.locator('button[data-test="remove-sauce-labs-onesie"]')
        self.remove_redshirt_from_cart_button = page.locator('button[data-test="remove-test.allthethings()-t-shirt-(red)"]')

        ### Method to remove all items from the cart page
    def remove_all_from_cart_page(self):
        self.remove_redshirt_from_cart_button.click()
        self.remove_jacket_from_cart_button.click()
        self.remove_onesie_from_cart_button.click()
        self.remove_tshirt_from_cart_button.click()
        self.remove_backpack_from_cart_button.click()
        self.remove_bikelight_from_cart_button.click()

        ### Method to remove 2 items from the cart page
    def remove_two_items_from_cart_page(self):
        self.remove_onesie_from_cart_button.click()
        self.remove_tshirt_from_cart_button.click()

        ### Method to redirect user from the Cart to the Inventory page
    def continue_shopping(self):
        self.continue_shopping_button.click()

        ### Method to proceed to Checkout page
    def go_to_the_checkout_page(self):
        self.checkout_button.click()


