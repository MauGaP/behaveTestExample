import time

from behave import given, when, then

from CommonConstants import product_name, product_price, product_description, product_added_message
from HomeSteps import click_first_product_displayed
from ProductPage import get_first_product_information, product_name_css_selector, product_price_css_selector, \
    product_description_css_selector, add_to_cart_button_css_selector
from Utils import click_element_by_css_selector, validate_alert_message
from Utils import locate_element_by_css_selector


@given('the user already added one product to the cart')
def product_already_added_to_cart(context):
    click_first_product_displayed(context)
    # TODO find a way to replace this sleep
    time.sleep(1)
    add_product_to_cart(context)


@when('adds the product to the cart')
def add_product_to_cart(context):
    click_element_by_css_selector(context, add_to_cart_button_css_selector)


@then('the page displays all the information correctly for the first item in {category}')
def product_page_information_displayed_correctly(context, category):
    # get first product attributes from dictionary
    product_information_dictionary = get_first_product_information(category)

    # get first product attributes from page
    product_information_from_page_dictionary = {}
    product_name_element_text = locate_element_by_css_selector(context, product_name_css_selector).text
    product_information_from_page_dictionary[product_name] = product_name_element_text
    product_price_element_text = locate_element_by_css_selector(context, product_price_css_selector).text
    product_information_from_page_dictionary[product_price] = product_price_element_text
    product_description_element_text = locate_element_by_css_selector(context, product_description_css_selector).text
    product_information_from_page_dictionary[product_description] = product_description_element_text

    # compare attributes
    assert product_information_dictionary == product_information_from_page_dictionary


@then('the page displays a confirmation message alert')
def product_added_confirmation_message(context):
    time.sleep(2)
    validate_alert_message(context, product_added_message)
