from behave import given, when, then

from Driver import launch_browser
from HeaderPage import logout_button_id, login_button_id, sign_up_button_id
from Utils import click_element_by_id, locate_element_by_id


@given('the user opens the page demoblaze.com in {browser} browser.')
def navigate_to_home_page(context, browser):
    launch_browser(context, browser)
    context.driver.maximize_window()
    context.driver.get("https://demoblaze.com")


@when('the user tries to logout')
def user_tries_to_logout(context):
    click_element_by_id(context, logout_button_id)


@then('"login" and "sign up" buttons are displayed on the page')
def login_and_signup_buttons_are_displayed(context):
    locate_element_by_id(context, login_button_id).is_displayed()
    locate_element_by_id(context, sign_up_button_id).is_displayed()
