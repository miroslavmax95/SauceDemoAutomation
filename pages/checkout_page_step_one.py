from playwright.sync_api import Page

class CheckoutPageOne:

    def __init__(self, page: Page):

        ### Checkout - step one, buttons and fields locators
        self.page = page
        self.first_name_field = page.get_by_placeholder('First Name')
        self.last_name_field = page.get_by_placeholder('Last Name')
        self.zip_number_field = page.get_by_placeholder('Zip/Postal Code')
        self.cancel_button = page.get_by_role('button', name='Cancel')
        self.continue_button = page.get_by_role('button', name='Continue')
        self.first_name_error = page.get_by_text('Error: First Name is required')
        self.last_name_error = page.get_by_text('Error: Last Name is required')
        self.zip_number_error = page.get_by_text('Error: Postal Code is required')

        ### Method to fill in the first name
    def fill_in_first_name(self, name: str):
        self.first_name_field.fill(name)

        ### Method to fill in the last name
    def fill_in_last_name(self,last_name: str):
        self.last_name_field.fill(last_name)

        ### Method to fill in te zip number
    def fill_in_zip_number(self, zip_no: str):
        self.zip_number_field.fill(zip_no)

        ### Method to fill in all customer data at once
    def fill_all_data(self, name: str, last_name: str, zip_no: str):
        self.first_name_field.fill(name)
        self.last_name_field.fill(last_name)
        self.zip_number_field.fill(zip_no)

        ### Method to navigate back to Cart page from Checkout step One
    def go_back_to_cart_via_cancel_button(self):
        self.cancel_button.click()

        ### Method to proceed to Checkout step Two
    def proceed_to_step_two_via_continue_button(self):
        self.continue_button.click()

