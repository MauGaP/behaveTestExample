Feature: Add products to cart

    As a common user
    I want to add products to cart
    In order to populate the cart

    Scenario: Adding products to the cart from inventory
        Given the user is on inventory page
        When the user adds a product to cart
        Then a new item is added to the cart