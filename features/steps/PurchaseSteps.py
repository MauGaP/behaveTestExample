from behave import then

from BasePage import send_keys_by_id, click_element_by_css_selector, locate_element_by_css_selector
from CommonConstants import purchase_name, purchase_country, purchase_city, purchase_credit_card_number, \
    purchase_credit_card_month, purchase_credit_card_year
from PurchasePage import name_field_id, country_field_id, city_field_id, credit_card_field_id, card_month_field_id, \
    card_year_field_id, confirmation_button_css_selector, confirmation_modal_css_selector, error_modal_css_selector
from behave import then

from BasePage import send_keys_by_id, click_element_by_css_selector, locate_element_by_css_selector
from CommonConstants import purchase_name, purchase_country, purchase_city, purchase_credit_card_number, \
    purchase_credit_card_month, purchase_credit_card_year
from PurchasePage import name_field_id, country_field_id, city_field_id, credit_card_field_id, card_month_field_id, \
    card_year_field_id, confirmation_button_css_selector, confirmation_modal_css_selector, error_modal_css_selector


def fill_credit_card_form(self, dictionary):
    # fill form
    send_keys_by_id(self, name_field_id, dictionary.get(purchase_name))
    send_keys_by_id(self, country_field_id, dictionary.get(purchase_country))
    send_keys_by_id(self, city_field_id, dictionary.get(purchase_city))
    send_keys_by_id(self, credit_card_field_id, dictionary.get(purchase_credit_card_number))
    send_keys_by_id(self, card_month_field_id, dictionary.get(purchase_credit_card_month))
    send_keys_by_id(self, card_year_field_id, dictionary.get(purchase_credit_card_year))
    # click submit button
    click_element_by_css_selector(self, confirmation_button_css_selector)


@then('the page displays a purchase confirmation modal')
def purchase_confirmation_modal_displayed(context):
    assert locate_element_by_css_selector(context, confirmation_modal_css_selector).is_displayed()


@then('the page displays an error modal')
def purchase_error_modal(context):
    assert locate_element_by_css_selector(context, error_modal_css_selector).is_displayed()
