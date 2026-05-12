from playwright.sync_api import Page

class CheckoutPageTwo:

    def __init__(self, page: Page):
        self.page = page
        self.payment_information = page.locator('div[data-test="payment-info-label"]')
        self.shipping_information = page.locator('div[data-test="shipping-info-value"]')
        self.total_value = page.locator('div[data-test="total-label"]')
        self.cancel_button = page.get_by_role('button', name='Cancel')
        self.finish_button = page.get_by_role('button', name='Finish')

    def go_back_to_step_one_via_cancel_button(self):
        self.cancel_button.click()

    def finish_checkout(self):
        self.finish_button.click()


