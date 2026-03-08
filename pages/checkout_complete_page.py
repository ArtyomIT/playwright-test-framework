from .base_page import BasePage
from playwright.sync_api import Page

class CheckoutCompletePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.back_home_button = page.get_by_role('button', name = 'Back Home')
        self.successful_text = page.locator('[data-test = "complete-header"]')

    def go_to_home(self):
        self.back_home_button.click()