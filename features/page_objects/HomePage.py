# region categories
from CommonConstants import phones_list, laptops_list, monitors_list, default_list

categories_css_selector = '#cat.list-group-item'
phones_css_selector = '.list-group .list-group-item:nth-child(2)'
laptops_css_selector = '.list-group .list-group-item:nth-child(3)'
monitors_css_selector = '.list-group .list-group-item:nth-child(4)'


def category_selection(category):
    match category.lower():
        case 'phones':
            return phones_css_selector
        case 'laptops':
            return laptops_css_selector
        case 'monitors':
            return monitors_css_selector
        case 'default':
            return categories_css_selector
        case _:
            print('not a valid selector')
# endregion categories


# region product list
def product_names_list(category):
    match category.lower():
        case 'phones':
            return phones_list
        case 'laptops':
            return laptops_list
        case 'monitors':
            return monitors_list
        case 'default':
            return default_list
        case _:
            print('not a valid category')


product_item_class_name = 'hrefch'
first_product_displayed = '#tbodyid .hrefch'
# endregion product list
