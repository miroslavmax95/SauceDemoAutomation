from playwright.sync_api import Page

class InventoryPage:

    def __init__(self, page: Page):

        ### Inventory page buttons
        self.page = page
        self.title = page.locator('span[data-test="title"]')
        self.logout_button = page.get_by_role('link', name='Logout')
        self.shopping_cart_badge = page.locator('span[data-test="shopping-cart-badge"]')
        self.shopping_cart_page_button = page.locator('a[data-test="shopping-cart-link"]')

        ### Add to cart buttons, each item has unique Add button on the page
        self.add_backpack_button = page.locator('button[data-test="add-to-cart-sauce-labs-backpack"]')
        self.add_bike_light_button = page.locator('button[data-test="add-to-cart-sauce-labs-bike-light"]')
        self.add_tshirt = page.locator('button[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
        self.add_jacket = page.locator('button[data-test="add-to-cart-sauce-labs-fleece-jacket"]')
        self.add_onesie = page.locator('button[data-test="add-to-cart-sauce-labs-onesie"]')
        self.add_redshirt = page.locator('button[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')

        ### Remove from cart buttons, when added each item has unique Remove button on the page
        self.remove_backpack_button = page.locator('button[data-test="remove-sauce-labs-backpack"]')
        self.remove_bike_light_button = page.locator('button[data-test="remove-sauce-labs-bike-light"]')
        self.remove_tshirt_button = page.locator('button[data-test="remove-sauce-labs-bolt-t-shirt"]')
        self.remove_jacket_button = page.locator('button[data-test="remove-sauce-labs-fleece-jacket"]')
        self.remove_onesie_button = page.locator('button[data-test="remove-sauce-labs-onesie"]')
        self.remove_redshirt_button = page.locator('button[data-test="remove-test.allthethings()-t-shirt-(red)"]')

        ### Hamburger menu & dropdown options
        self.hamburger_menu = page.get_by_role('button', name='Open menu')
        self.hamburger_all_items_option = page.locator('a[data-test="inventory-sidebar-link"]')
        self.hamburger_about_option = page.locator('a[data-test="about-sidebar-link"]')
        self.hamburger_logout_option = page.locator('a[data-test="logout-sidebar-link"]')


        ### Method that adds all available items to the cart
    def add_all_items_to_the_cart(self):
        self.add_backpack_button.click()
        self.add_bike_light_button.click()
        self.add_redshirt.click()
        self.add_tshirt.click()
        self.add_onesie.click()
        self.add_jacket.click()

        ### Method to add 3 items to the cart
    def add_three_items_to_the_cart(self):
        self.add_jacket.click()
        self.add_tshirt.click()
        self.add_bike_light_button.click()

        ### Method to remove all items from the cart, per item
    def remove_all_items_from_cart(self):
        self.remove_jacket_button.click()
        self.remove_bike_light_button.click()
        self.remove_backpack_button.click()
        self.remove_onesie_button.click()
        self.remove_redshirt_button.click()
        self.remove_tshirt_button.click()

        ### Method to remove 3 items from the cart, per item
    def remove_three_items_from_cart(self):
        self.remove_onesie_button.click()
        self.remove_redshirt_button.click()
        self.remove_tshirt_button.click()

        ### Method to open the Cart page
    def open_shopping_cart_page(self):
        self.shopping_cart_page_button.click()

        ### Method to open the Hamburger menu
    def open_hamburger_menu(self):
        self.hamburger_menu.click()

        ### Method to navigate user to the Inventory page via Hamburger menu
    def hamburger_inventory_page(self):
        self.hamburger_menu.click()
        self.hamburger_all_items_option.click()

        ### Method to navigate user to the About page via Hamburger menu
    def hamburger_about_page(self):
        self.hamburger_menu.click()
        self.hamburger_about_option.click()

        ### Method to logout and terminate current session via Hamburger menu
    def hamburger_logout(self):
        self.hamburger_menu.click()
        self.hamburger_logout_option.click()



    
