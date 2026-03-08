import pytest
from pages.login_page import LoginPage
from pages.items_page import ItemsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def items_page(page):
    return ItemsPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)

@pytest.fixture
def overview_page(page):
    return OverviewPage(page)

@pytest.fixture
def checkout_complete_page(page):
    return CheckoutCompletePage(page)