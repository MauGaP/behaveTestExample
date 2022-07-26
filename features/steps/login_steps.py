from behave import given, then, when
from features.page_objects.BasePage import (click_element_by_css_selector,
                                            send_keys_by_css_selector,
                                            wait_until_url_changes)
from features.page_objects.login_page import (LOGIN_BTN, LOGIN_LOGO,
                                              PASSWORD_FIELD, USERNAME_FIELD)
from page_objects.login_page import LOGIN_URL
from utils.Driver import launch_browser


@given('the user is on SauceLabs page')
def navigate_to_saucelabs(context) :
    launch_browser(context, 'Chrome')
    context.driver.maximize_window()
    context.driver.get(LOGIN_URL)

@when('the user logs in with valid credentials')
def login_with_valid_credentials(context) :
    send_keys_by_css_selector(context, USERNAME_FIELD, 'standard_user')
    send_keys_by_css_selector(context, PASSWORD_FIELD, 'secret_sauce')
    click_element_by_css_selector(context, LOGIN_BTN)
    
@then('the user is redirected to the home of the application')
def user_is_redirected_to_home(context) :
    wait_until_url_changes(context)
    current_url = context.driver.current_url
    assert 'https://www.saucedemo.com/inventory.html' == current_url
