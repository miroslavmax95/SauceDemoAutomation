from playwright.sync_api import Page

class CheckoutComplete:

    def __init__(self, page: Page):

        ### Checkout complete page buttons and fields locators
        self.page = page
        self.checkout_complete_message = page.get_by_text('Your order has been dispatched, and will arrive just as fast as the pony can get there!')
        self.back_home_button = page.get_by_role('button', name='Back Home')

        ### Method to navigate back to Inventory page when the Checkout is completed
    def go_back_home_after_checkout(self):
        self.back_home_button.click()

