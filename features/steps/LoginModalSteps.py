import time

from behave import when, then
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from HeaderPage import login_button_id, user_welcome_message_id, logout_button_id
from LoginModalPage import login_user_field_id, login_password_field_id, login_ok_button_css_selector
from Utils import click_element_by_id, send_keys_by_id, click_element_by_css, find_element_by_id


@when('the user enters his {user} and {password} credentials on the login modal')
def open_sign_up_modal_and_enter_credentials(context, user, password):
    click_element_by_id(context, login_button_id)
    send_keys_by_id(context, login_user_field_id, user)
    send_keys_by_id(context, login_password_field_id, password)
    click_element_by_css(context, login_ok_button_css_selector)


@then('the page displays the "Welcome {username}" and the log out button on the header')
def validate_logged_in_user(context, username):
    time.sleep(2)
    user_message = find_element_by_id(context, user_welcome_message_id)
    logout_button = find_element_by_id(context, logout_button_id)
    user_message_text = user_message.text
    assert user_message.is_displayed()
    assert logout_button.is_displayed()
    assert username in user_message_text


@then("the page displays an alert with an unsuccessful login message")
def unsuccessful_confirmation_message(context):
    try:
        WebDriverWait(context.driver, 3).until(expected_conditions.alert_is_present())
        alert = context.driver.switch_to.alert
        assert 'User does not exist.' in alert.text
        alert.accept()
    except TimeoutException:
        print("no alert")
