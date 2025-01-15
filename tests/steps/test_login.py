import pytest
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage
from utils.driver_manager import create_driver

scenarios('../../../features/login.feature')

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

@given("User is on the login page")
def user_on_login_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    return login_page  # penting untuk meneruskan instance LoginPage

@when('User enters valid username "{username}" and valid password "{password}"')
def user_enters_valid_credentials(login_page, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)

@when('User enters invalid username "{username}" and valid password "{password}"')
def user_enters_invalid_username(login_page, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)

@when('User enters valid username "{username}" and invalid password "{password}"')
def user_enters_invalid_password(login_page, username, password):
    login_page.enter_username(username)
    login_page.enter_password(password)

@when("User clicks the login button")
def user_clicks_login_button(login_page):
    login_page.click_login()

@then('User should be logged in successfully and see "{message}"')
def user_should_be_logged_in(login_page, message, driver):
    assert message in login_page.get_success_message()

@then('User should see an error message "{message}"')
def user_should_see_error_message(login_page, message):
  assert message in login_page.get_error_message()