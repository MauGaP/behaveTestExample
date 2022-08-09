from behave import when, then
from features.page_objects.BasePage import get_element_text
from features.page_objects.inventory_page import ADD_BACKPACK_TO_CART_BTN, FILTER_BTN, FIRST_INVENTORY_ELEMENT
from page_objects.BasePage import click_element_by_css_selector

@when('the user adds a product to cart')
def add_product_from_inventory_page_to_cart(context) :
    click_element_by_css_selector(context, ADD_BACKPACK_TO_CART_BTN)

@when('the user select an {optionFilter}')
def select_option_filter(context, optionFilter) :
    click_element_by_css_selector(context, FILTER_BTN)
    click_element_by_css_selector(context, optionFilter)

@then('first product displayed is {firstItemTitle}')
def validate_inventory_list(context, firstItemTitle) :
    title_text = get_element_text(context, FIRST_INVENTORY_ELEMENT)
    print(title_text)
    print(firstItemTitle)
    assert title_text == firstItemTitle
    