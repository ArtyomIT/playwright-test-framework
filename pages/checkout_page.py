from .base_page import BasePage
from playwright.sync_api import Page

class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.first_name_field = page.get_by_placeholder('First Name')
        self.last_name_field = page.get_by_placeholder('Last Name')
        self.zip_code_field = page.get_by_placeholder('Zip/Postal Code')
        self.continue_button = page.get_by_role('button', name='Continue')

    def fill_form(self, first_name, last_name, zip_code):
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.zip_code_field.fill(zip_code)

    def continue_button_click(self):
        self.continue_button.click()