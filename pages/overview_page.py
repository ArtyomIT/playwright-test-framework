from .base_page import BasePage
from playwright.sync_api import Page

class OverviewPage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.finish_button = page.locator('[data-test = "finish"]')

    def finish_button_click(self):
        self.finish_button.click()