from behave import given, when, then
from selenium.webdriver.common.by import By

from page_objects.BasePage import click_element_by_id, send_keys_by_id, click_element_by_css_selector, \
    locate_element_by_id, validate_alert_message, wait_until_element_displayed
from page_objects.HeaderPage import login_button_id, user_welcome_message_id, logout_button_id
from page_objects.LoginModalPage import login_user_field_id, login_password_field_id, login_ok_button_css_selector
from utils.CommonConstants import user_does_not_exist_message, demo_user, demo_password


@given('an existing user is already logged in')
@when('the user enters his {user} and {password} credentials on the login modal')
def open_sign_up_modal_and_enter_credentials(context, user=None, password=None):
    if user is None and password is None:
        user = demo_user
        password = demo_password
    click_element_by_id(context, login_button_id)
    send_keys_by_id(context, login_user_field_id, user)
    send_keys_by_id(context, login_password_field_id, password)
    click_element_by_css_selector(context, login_ok_button_css_selector)


@then('the page displays the "Welcome {username}" and the log out button on the header')
def validate_logged_in_user(context, username):
    wait_until_element_displayed(context, (By.ID, user_welcome_message_id))
    user_message = locate_element_by_id(context, user_welcome_message_id)
    logout_button = locate_element_by_id(context, logout_button_id)
    user_message_text = user_message.text
    assert user_message.is_displayed()
    assert logout_button.is_displayed()
    assert username in user_message_text


@then("the page displays an alert with an unsuccessful login message")
def unsuccessful_confirmation_message(context):
    assert validate_alert_message(context, user_does_not_exist_message)
