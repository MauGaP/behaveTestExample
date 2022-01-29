from behave import given

from Driver import launch_browser


@given('the {browser} browser is located on demoblaze.com')
def navigate_to_home_page(context, browser):
    launch_browser(context, browser)
    context.driver.get("https://demoblaze.com")
