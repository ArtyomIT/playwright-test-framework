from playwright.sync_api import Page
from .base_page import BasePage

class ItemsPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.all_elements = page.locator('.inventory_item')
        self.cart = page.locator('[data-test="shopping-cart-badge"]') 
        self.sort_select = page.locator('[data-test="product-sort-container"]')
        self.item_names = page.locator('.inventory_item_name')
        self.item_prices = page.locator('.inventory_item_price')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]') 

    def get_count_elements(self):
        return self.all_elements.count()

    def add_first_element_to_cart(self):
        self.all_elements.first.locator('button').click()

    def add_two_element_to_cart(self):
        self.all_elements.nth(0).locator('button').click()
        self.all_elements.nth(1).locator('button').click()

    def add_all_elements_to_cart(self):
        for i in range(self.get_count_elements()):
            self.all_elements.nth(i).locator('button').click()

    def remove_all_elements_to_cart(self):
        for i in range(self.get_count_elements()):
            button = self.all_elements.nth(i).locator('button') 
            if button.inner_text() == 'Remove':
                button.click()  

    def sort_by(self, value: str) -> None:
        self.sort_select.select_option(value)

    def get_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def get_prices(self) -> list[float]:
        prices_text = self.item_prices.all_inner_texts()  
        return [float(p.replace("$", "").strip()) for p in prices_text]

    def go_to_cart(self):
        self.cart_link.click()
