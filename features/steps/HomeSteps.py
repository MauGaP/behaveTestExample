import time

from behave import when, then
from selenium.webdriver.common.by import By

from page_objects.BasePage import click_element_by_css_selector, locate_elements_by_class, wait_until_url_changes, \
    wait_until_element_displayed
from page_objects.HomePage import category_selection, product_item_class_name, filter_product_names_list, \
    first_product_displayed


@when('the user filters {category}')
def user_filters_category(context, category):
    category_selector = category_selection(category)
    time.sleep(2)
    wait_until_element_displayed(context, (By.CSS_SELECTOR, category_selector))
    click_element_by_css_selector(context, category_selector)


@when('selects the first product displayed')
def click_first_product_displayed(context):
    click_element_by_css_selector(context, first_product_displayed)
    wait_until_url_changes(context)


@then('the page only displays {category} items')
def page_displays_selected_category(context, category):
    # TODO find a way to replace this sleep
    time.sleep(1)

    # get list of product names
    list_of_product_names = filter_product_names_list(category)
    list_of_product_names.sort()

    # create a list of text contained in page elements
    list_of_product_names_from_page = []
    wait_until_element_displayed(context, (By.CLASS_NAME, product_item_class_name))
    for product_element in locate_elements_by_class(context, product_item_class_name):
        list_of_product_names_from_page.append(product_element.text)
    list_of_product_names_from_page.sort()

    # validate text elements equal text from product name list
    assert list_of_product_names == list_of_product_names_from_page
    time.sleep(2)
