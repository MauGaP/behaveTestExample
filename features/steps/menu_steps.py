from behave import when
from features.page_objects.menu_page import BOTON_LOGOUT, BOTON_MENU
from features.page_objects.BasePage import click_element_by_css_selector



@when('the user logs out')
def user_logs_out(context) :
    click_element_by_css_selector(context, BOTON_MENU)
    click_element_by_css_selector(context, BOTON_LOGOUT)