from behave import given, when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from driver import launch_browser
from signup_page import sign_up_button_id, sign_up_user_field_id, sign_up_password_field_id
from utils import click_element_by_id, click_element_by_css, send_keys_by_id


@given('the {browser} browser is located on demoblaze.com')
def navigate_to_home_page(context, browser):
    launch_browser(context, browser)
    context.driver.get("https://demoblaze.com")


@when('the user registers his {user} and {password} credentials on the sign up modal')
def open_sign_up_modal_and_enter_credentials(context, user, password):
    click_element_by_id(context, sign_up_button_id)
    send_keys_by_id(context, sign_up_user_field_id, user)
    send_keys_by_id(context, sign_up_password_field_id, password)
    click_element_by_css(context, "#signInModal button.btn-primary")

    # This method should include a "delete user" function as a clean up after its execution. This is something that
    # I can't do since I have no access to any delete user method on the page


@then('the page displays an alert modal with a successful confirmation message')
def successful_confirmation_message(context):
    try:
        WebDriverWait(context.driver, 3).until(expected_conditions.alert_is_present())
        alert = context.driver.switch_to.alert
        assert 'Sign up successful.' in alert.text
        alert.accept()
    except TimeoutException:
        print("no alert")

@then('the page displays an alert modal with an unsuccessful message')
def unsuccessful_confirmation_message(context):
    try:
        WebDriverWait(context.driver, 3).until(expected_conditions.alert_is_present())
        alert = context.driver.switch_to.alert
        assert 'This user already exist.' in alert.text
        alert.accept()
    except TimeoutException:
        print("no alert")
