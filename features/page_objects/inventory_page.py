ADD_BACKPACK_TO_CART_BTN = '#add-to-cart-sauce-labs-backpack'

CART_BTN = '#shopping_cart_container > a'

FILTER_BTN = '#header_container > div.header_secondary_container > div.right_component > span > select'

FIRST_INVENTORY_ELEMENT = '.inventory_list > div:nth-child(1) .inventory_item_name'

def filter_selector(filterOption):
    match filterOption :
        case "Name (A to Z)":
            return "#header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(1)"
        case "Name (Z to A)":
            return "#header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(2)"
        case "Price (low to high)":
            return "#header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(3)"
        case "Price (high to low)":
            return "#header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(4)"
        case _:
            print("ERROR: not valid")