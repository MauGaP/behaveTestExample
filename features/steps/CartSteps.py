import time

from behave import when, then

from CartPage import delete_first_product_button, cart_products_css_selector, purchase_button_css_selector
from CommonConstants import purchase_data_dictionary
from HeaderPage import cart_button_id
from PurchaseSteps import fill_credit_card_form
from Utils import click_element_by_css_selector, click_element_by_id, locate_elements_by_css_selector


@when('the user deletes the product from the cart')
def delete_product_from_cart(context):
    # TODO find a way to replace this sleep
    time.sleep(2)
    # close alert
    alert = context.driver.switch_to.alert
    alert.accept()
    # navigate to cart
    click_element_by_id(context, cart_button_id)
    # eliminate product
    click_element_by_css_selector(context, delete_first_product_button)


@when('the user places the order')
def place_order(context):
    click_element_by_id(context, cart_button_id)
    click_element_by_css_selector(context, purchase_button_css_selector)
    fill_credit_card_form(context, purchase_data_dictionary)


@then('the page displays an empty cart')
def validate_cart_is_empty(context):
    # TODO find a way to replace this sleep
    time.sleep(2)
    list_of_cart_products = locate_elements_by_css_selector(context, cart_products_css_selector)

    # Empty lists are considered a False boolean in Python
    assert not list_of_cart_products