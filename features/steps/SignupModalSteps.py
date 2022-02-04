from behave import when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from CommonConstants import sign_up_successful_message, this_user_already_exists_message
from HeaderPage import sign_up_button_id
from SignupModalPage import sign_up_user_field_id, sign_up_password_field_id, sign_up_ok_button_css_selector
from Utils import click_element_by_id, send_keys_by_id, click_element_by_css, validate_alert_message


@when('the user registers his {username} and {password} credentials on the sign up modal')
def open_sign_up_modal_and_enter_credentials(context, username, password):
    click_element_by_id(context, sign_up_button_id)
    send_keys_by_id(context, sign_up_user_field_id, username)
    send_keys_by_id(context, sign_up_password_field_id, password)
    click_element_by_css(context, sign_up_ok_button_css_selector)


@then("the page displays an alert with a successful confirmation message")
# This method should include a "delete user" function as a cleanup after its execution. This is something that
# I can't do since I have no access to any delete user method on the page
def successful_confirmation_message(context):
    validate_alert_message(context, sign_up_successful_message)


@then("the page displays an alert with an unsuccessful signup message")
def unsuccessful_confirmation_message(context):
    validate_alert_message(context, this_user_already_exists_message)
