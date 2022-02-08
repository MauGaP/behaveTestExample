import time

from behave import when, then

from HomePage import category_selection, product_item_class_name, filter_product_names_list, \
    first_product_displayed
from Utils import click_element_by_css_selector, locate_elements_by_class


@when('the user filters {category}')
def user_filters_category(context, category):
    category_selector = category_selection(category)
    click_element_by_css_selector(context, category_selector)


@when('selects the first product displayed')
def click_first_product_displayed(context):
    click_element_by_css_selector(context, first_product_displayed)
    # TODO find a way to replace this sleep
    time.sleep(2)


@then('the page only displays {category} items')
def page_displays_selected_category(context, category):
    # TODO find a way to replace this sleep
    time.sleep(2)

    # get list of product names
    list_of_product_names = filter_product_names_list(category)
    list_of_product_names.sort()

    # create a list of text contained in page elements
    list_of_product_names_from_page = []
    for product_element in locate_elements_by_class(context, product_item_class_name):
        list_of_product_names_from_page.append(product_element.text)
    list_of_product_names_from_page.sort()

    # validate text elements equal text from product name list
    assert list_of_product_names == list_of_product_names_from_page
    time.sleep(2)
