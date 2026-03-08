from .base_page import BasePage
from playwright.sync_api import Page

class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = page.get_by_role('button', name='Checkout')

    def checkout_button_click(self):
        self.checkout_button.click()