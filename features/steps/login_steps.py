from login import click_element_by_css_selector()

@Given('the user is on login page')
def user_navigates_to_login()
    click_element_by_css_selector(LOGIN_BUTTON)

@When('The user enters valid credentials')
def user_enters_credentials()
    