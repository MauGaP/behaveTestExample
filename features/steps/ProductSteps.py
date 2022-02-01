from behave import then

from ProductPage import get_first_product_information, product_name_css_selector, product_price_css_selector, \
    product_description_css_selector
from Utils import locate_element_by_css
from behave import then

from ProductPage import get_first_product_information, product_name_css_selector, product_price_css_selector, \
    product_description_css_selector
from Utils import locate_element_by_css


@then('the page displays all the information correctly for the first item in {category}')
def product_page_information_displayed_correctly(context, category):
    # get first product attributes from dictionary
    product_information_dictionary = get_first_product_information(category)

    # get first product attributes from page
    product_information_from_page_dictionary = {}
    product_name = locate_element_by_css(context, product_name_css_selector).text
    product_information_from_page_dictionary['product_name'] = product_name
    product_price = locate_element_by_css(context, product_price_css_selector).text
    product_information_from_page_dictionary['product_price'] = product_price
    product_description = locate_element_by_css(context, product_description_css_selector).text
    product_information_from_page_dictionary['product_description'] = product_description

    # compare attributes
    assert product_information_dictionary == product_information_from_page_dictionary
