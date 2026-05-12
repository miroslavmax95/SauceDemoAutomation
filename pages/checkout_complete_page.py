from playwright.sync_api import Page

class CheckoutComplete:

    def __init__(self, page: Page):
        self.page = page
        self.checkout_complete_message = page.get_by_text('Your order has been dispatched, and will arrive just as fast as the pony can get there!')
        self.back_home_button = page.get_by_role('button', name='Back Home')

    def go_back_home_after_checkout(self):
        self.back_home_button.click()

