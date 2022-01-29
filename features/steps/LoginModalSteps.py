# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# from LoginModalPage import
# from Utils import click_element_by_id, send_keys_by_id, click_element_by_css
#
#
# @when('the user registers his {user} and {password} credentials on the login up modal')
# def open_sign_up_modal_and_enter_credentials(context, user, password):
#     click_element_by_id(context, log_in_button_id)
#     send_keys_by_id(context, log_in_user_field_id, user)
#     send_keys_by_id(context, log_in_password_field_id, password)
#     click_element_by_css(context, log_in_ok_button_css_selector)
#
#
# @then('the page displays an alert modal with an unsuccessful login message')
# def unsuccessful_confirmation_message(context):
#     try:
#         WebDriverWait(context.driver, 3).until(expected_conditions.alert_is_present())
#         alert = context.driver.switch_to.alert
#         assert 'This user already exist.' in alert.text
#         alert.accept()
#     except TimeoutException:
#         print("no alert")
