Feature: Sort products on inventory 

    As a common user
    I want to sort products on inventory
    In order to see a specific order of products 

    Scenario Outline: Sort products on inventory 
        Given the user is on inventory page
        When the user select an <optionFilter>
        Then first product displayed is <firstItemTitle>

    Examples:
        | optionFilter | firstItemTitle |
        |  #header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(1)  | Sauce Labs Backpack |
        |  #header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(2)  | Test.allTheThings() T-Shirt (Red) |
        |  #header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(3)  | Sauce Labs Onesie |
        |  #header_container > div.header_secondary_container > div.right_component > span > select > option:nth-child(4)  | Sauce Labs Fleece Jacket |