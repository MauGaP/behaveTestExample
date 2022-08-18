from behave import given, then, when
from features.page_objects.BasePage import get_element_text
from features.page_objects.cart_page import BACKPACK_PRODUCT_TEXT
from features.page_objects.inventory_page import ADD_BACKPACK_TO_CART_BTN, FILTER_BTN, FIRST_INVENTORY_ELEMENT, CART_BTN, filter_selector
from page_objects.BasePage import click_element_by_css_selector

@given('the user has an item in the cart')
def product_in_cart(context) :
    click_element_by_css_selector(context, ADD_BACKPACK_TO_CART_BTN)
    click_element_by_css_selector(context, CART_BTN)

@when('the user adds a product to cart')
def add_product_from_inventory_page_to_cart(context) :
    click_element_by_css_selector(context, ADD_BACKPACK_TO_CART_BTN)

@when('the user select an {optionFilter}')
def select_option_filter(context, optionFilter) :
    click_element_by_css_selector(context, FILTER_BTN)
    click_element_by_css_selector(context, filter_selector(optionFilter))

@then('first product displayed is {firstItemTitle}')
def validate_inventory_list(context, firstItemTitle) :
    title_text = get_element_text(context, FIRST_INVENTORY_ELEMENT)
    print(title_text)
    print(firstItemTitle)
    assert title_text == firstItemTitle
    
@then('a new item is added to the cart')
def validate_product_added_to_cart(context) :
    click_element_by_css_selector(context, CART_BTN)
    title_text = get_element_text(context, BACKPACK_PRODUCT_TEXT)
    print(title_text)
    assert title_text == 'Sauce Labs Backpack'
    