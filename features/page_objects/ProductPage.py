# region product information
from CommonConstants import first_phone_dictionary, first_laptop_dictionary, first_monitor_dictionary, \
    first_product_dictionary

product_name_css_selector = '#tbodyid .name'
product_price_css_selector = '#tbodyid .price-container'
product_description_css_selector = '#more-information > p'
add_to_cart_button_css_selector = '#tbodyid .btn-success'


def get_first_product_information(category):
    match category.lower():
        case 'phones':
            return first_phone_dictionary
        case 'laptops':
            return first_laptop_dictionary
        case 'monitors':
            return first_monitor_dictionary
        case 'default':
            return first_product_dictionary
        case _:
            print('not a valid entry')
# endregion product information
