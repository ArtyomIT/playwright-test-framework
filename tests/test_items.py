import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_add_all_elements_to_cart(login_page, items_page):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')
    count_elements = items_page.get_count_elements()
    items_page.add_all_elements_to_cart()
    expect(items_page.cart).to_have_text(str(count_elements))

@pytest.mark.smoke
@pytest.mark.positive
@pytest.mark.regression
def test_remove_all_elements_from_cart(login_page, items_page):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')
    count_elements = items_page.get_count_elements()
    items_page.add_all_elements_to_cart()
    expect(items_page.cart).to_have_text(str(count_elements))
    items_page.remove_all_elements_to_cart() 
    expect(items_page.cart).to_have_count(0)

@pytest.mark.positive
@pytest.mark.regression
@pytest.mark.parametrize(
    "sort_value, key",
    [
        pytest.param("az", "name_asc", id="name_asc"),
        pytest.param("za", "name_desc", id="name_desc"),
        pytest.param("lohi", "price_asc", id="price_asc"),
        pytest.param("hilo", "price_desc", id="price_desc"),
    ]
)
def test_inventory_sorting(login_page, items_page, sort_value, key):
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    items_page.sort_by(sort_value)

    if "name" in key:
        actual = items_page.get_names()
        expected = sorted(actual, reverse=("desc" in key))
    else:
        actual = items_page.get_prices()
        expected = sorted(actual, reverse=("desc" in key))

    assert actual == expected, f"Sorting '{sort_value}' broken. Actual: {actual}"