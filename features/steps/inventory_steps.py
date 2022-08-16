from behave import then, when
from features.page_objects.cart_page import BACKPACK_PRODUCT_TEXT
from features.page_objects.BasePage import get_element_text
from features.page_objects.inventory_page import ADD_BACKPACK_TO_CART_BTN, CART_BTN, PRODUCT_BACKPACK_TITLE
from page_objects.BasePage import click_element_by_css_selector, wait_until_url_changes


@given('el usuario tiene un producto en el carrito')
def product_in_cart(context) :
    click_element_by_css_selector(context, ADD_BACKPACK_TO_CART_BTN)
    click_element_by_css_selector(context, CART_BTN)

@when('the user adds a product to cart')
def add_product_from_inventory_page_to_cart(context) :
    click_element_by_css_selector(context, ADD_BACKPACK_TO_CART_BTN)

@when('the user select a product')
def user_select_product(context) :
    click_element_by_css_selector(context, PRODUCT_BACKPACK_TITLE)
    
  
@then('a new item is added to the cart')
def validate_product_in_cart(context) :
    click_element_by_css_selector(context, CART_BTN)
    title_text =get_element_text(context, TITLE_PRODUCT)
    print(title_text)
    assert title_text == 'Sauce Labs Backpack'
    time.sleep(10)
