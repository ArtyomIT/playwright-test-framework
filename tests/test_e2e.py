import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_successful_order_with_one_item(login_page, items_page, cart_page, checkout_page, overview_page, checkout_complete_page):
    # Login
    login_page.open()
    expect(login_page.page).to_have_url("https://www.saucedemo.com/")
    login_page.login('standard_user', 'secret_sauce')

    # Items page
    expect(items_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    items_page.add_first_element_to_cart()
    items_page.go_to_cart()

    # Cart page
    expect(cart_page.page).to_have_url("https://www.saucedemo.com/cart.html")
    cart_page.checkout_button_click()

    # Checkout page
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout_page.fill_form('Test', 'User', '123456')
    checkout_page.continue_button_click()

    # Overview page
    expect(overview_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    overview_page.finish_button_click()

    # Complete page
    expect(checkout_complete_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(checkout_complete_page.successful_text).to_have_text('Thank you for your order!')
    checkout_complete_page.go_to_home()

    # Back to items page
    expect(checkout_complete_page.page).to_have_url('https://www.saucedemo.com/inventory.html')

@pytest.mark.positive
@pytest.mark.regression
def test_successful_order_with_many_items(login_page, items_page, cart_page, checkout_page, overview_page, checkout_complete_page):
    # Login
    login_page.open()
    expect(login_page.page).to_have_url("https://www.saucedemo.com/")
    login_page.login('standard_user', 'secret_sauce')

    # Items page
    expect(items_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    items_page.add_all_elements_to_cart()
    items_page.go_to_cart()

    # Cart page
    expect(cart_page.page).to_have_url("https://www.saucedemo.com/cart.html")
    cart_page.checkout_button_click()

    # Checkout page
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkout_page.fill_form('Test', 'User', '123456')
    checkout_page.continue_button_click()

    # Overview page
    expect(overview_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    overview_page.finish_button_click()

    # Complete page
    expect(checkout_complete_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(checkout_complete_page.successful_text).to_have_text('Thank you for your order!')
    checkout_complete_page.go_to_home()

    # Back to items page
    expect(checkout_complete_page.page).to_have_url('https://www.saucedemo.com/inventory.html')

