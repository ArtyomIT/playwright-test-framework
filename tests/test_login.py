import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
@pytest.mark.auth
@pytest.mark.positive
def test_login_success(login_page):
    login_page.open()
    login_page.login('standard_user', 'secret_sauce')
    expect(login_page.page).to_have_url('https://www.saucedemo.com/inventory.html')

@pytest.mark.auth
@pytest.mark.negative
@pytest.mark.parametrize('username, password, expected_message', [
    pytest.param('standard_user', 'secret_sauce_wrong', 'Epic sadface: Username and password do not match any user in this service', id='wrong_password'),
    pytest.param('standard_user_wrong', 'secret_sauce', 'Epic sadface: Username and password do not match any user in this service', id='wrong_login'),
    pytest.param('locked_out_user', 'secret_sauce', 'Epic sadface: Sorry, this user has been locked out.', id='locked_user')
])
def test_login_fail(login_page, username, password, expected_message):
    login_page.open()
    login_page.login(username, password)
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(expected_message)



    
