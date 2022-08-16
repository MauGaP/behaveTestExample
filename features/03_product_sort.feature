Feature: Sort products on inventory 

    As a common user
    I want to sort products on inventory
    In order to see a specific order of products 

    Scenario Outline: Sort products on inventory with <optionFilter>
        Given the user is on inventory page
        When the user select an <optionFilter>
        Then first product displayed is <firstItemTitle>

    Examples:
        | optionFilter | firstItemTitle |
        |  Name (A to Z)  | Sauce Labs Backpack |
        |  Name (Z to A)  | Test.allTheThings() T-Shirt (Red) |
        |  Price (low to high)  | Sauce Labs Onesie |
        |  Price (high to low)  | Sauce Labs Fleece Jacket |