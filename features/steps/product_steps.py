from behave import given, when, then
from features.page_objects.login_page import (EXPECTEDHOME_URL, LOGIN_BTN, LOGIN_URL,
                                              PASSWORD_FIELD, USERNAME_FIELD)
from features.page_objects.BasePage import (click_element_by_css_selector,
                                            send_keys_by_css_selector,
                                            wait_until_url_changes,
                                            get_element_text)
from features.page_objects.product_page import PRODUCT_TITLE
import time


@then('information about the product is displayed')
def validate_title_product_selected(context) :
    title_text_product =get_element_text(context, PRODUCT_TITLE)
    print(title_text_product)
    assert title_text_product == 'Sauce Labs Backpack'
    time.sleep(5)