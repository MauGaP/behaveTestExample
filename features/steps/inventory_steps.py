from behave import given, then, when
from features.page_objects.BasePage import get_element_text
from features.page_objects.cart_page import BACKPACK_PRODUCT_TEXT
from features.page_objects.inventory_page import ADD_BACKPACK_TO_CART_BTN, CART_BTN
from page_objects.BasePage import click_element_by_css_selector
import time

@given('the user has an item in the cart')
def product_in_cart(context) :
    click_element_by_css_selector(context, ADD_BACKPACK_TO_CART_BTN)
    click_element_by_css_selector(context, CART_BTN)

@when('the user adds a product to cart')
def add_product_from_inventory_page_to_cart(context) :
    click_element_by_css_selector(context, ADD_BACKPACK_TO_CART_BTN)
    
@then('a new item is added to the cart')
def validate_product_added_to_cart(context) :
    click_element_by_css_selector(context, CART_BTN)
    title_text = get_element_text(context, BACKPACK_PRODUCT_TEXT)
    print(title_text)
    assert title_text == 'Sauce Labs Backpack'
    