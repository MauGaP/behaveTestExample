from pickle import TRUE
from behave import then, when
from features.page_objects.cart_page import CART_ITEM
from features.page_objects.compra_page import BOTON_CHECKOUT, BOTON_CONTINUE, BOTON_FINISH, FIRST_NAME, LAST_NAME, MENSAJE_COMPRA_EXITOSA, POSTAL_CODE, VALID_FIRST_NAME, VALID_LAST_NAME, VALID_POSTAL_CODE
from page_objects.BasePage import click_element_by_css_selector, send_keys_by_css_selector
from features.page_objects.BasePage import element_not_displayed, get_element_text
import time

@when('el usuario completa la compra')
def generate_purchase(context) :
    click_element_by_css_selector(context, BOTON_CHECKOUT)
    send_keys_by_css_selector(context, FIRST_NAME, VALID_FIRST_NAME)
    send_keys_by_css_selector(context, LAST_NAME, VALID_LAST_NAME)
    send_keys_by_css_selector(context, POSTAL_CODE, VALID_POSTAL_CODE)
    click_element_by_css_selector(context, BOTON_CONTINUE)
    click_element_by_css_selector(context, BOTON_FINISH)

@when('the user removes an item from the cart')
def remove_item(context) :
    click_element_by_css_selector(context, '#remove-sauce-labs-backpack')

@then('se muestra el mensaje de compra exitosa')
def SUCCESSFUL_PURCHASE_MESSAGE(context) :
    title_text = get_element_text(context, MENSAJE_COMPRA_EXITOSA)
    print(title_text)
    assert title_text == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'

@then('a new item is disappears from the cart')
def validate_element_deleted(context) :
   element_not_present = element_not_displayed(context, CART_ITEM)
   assert element_not_present == True
  
    