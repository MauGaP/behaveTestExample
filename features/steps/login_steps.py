from behave import given, then, when
from features.page_objects.BasePage import (click_element_by_css_selector,
                                            send_keys_by_css_selector,
                                            wait_until_url_changes)
from features.page_objects.login_page import (EXPECTEDHOME_URL, LOGIN_BTN, LOGIN_URL,
                                              PASSWORD_FIELD, USERNAME_FIELD)
from features.utils.CommonConstants import VALID_PASSWORD, VALID_USERNAME
from utils.Driver import launch_browser


@given('the user is on SauceLabs page')
def navigate_to_saucelabs(context) :
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)

@given('the user is on inventory page')
def user_already_logged_in(context) :
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)
    send_keys_by_css_selector(context, USERNAME_FIELD, VALID_USERNAME)
    send_keys_by_css_selector(context, PASSWORD_FIELD, VALID_PASSWORD)
    click_element_by_css_selector(context, LOGIN_BTN)

@when('the user logs in with valid credentials')
def login_with_valid_credentials(context) :
    send_keys_by_css_selector(context, USERNAME_FIELD, VALID_USERNAME)
    send_keys_by_css_selector(context, PASSWORD_FIELD, VALID_PASSWORD)
    click_element_by_css_selector(context, LOGIN_BTN)
    
    
@then('the user is redirected to the home of the application')
def user_is_redirected_to_home(context) :
    wait_until_url_changes(context)
    assert EXPECTEDHOME_URL == context.driver.current_url

@then('the user is redirected to login page')
def user_is_redirected_to_home(context) :
    wait_until_url_changes(context)
    assert LOGIN_URL == context.driver.current_url
