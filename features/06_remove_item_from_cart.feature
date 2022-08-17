Feature: Remove item from cart

    As a common user
    I want to remove products from the cart
    In order to empty the cart

    Background:
        Given the user is on inventory page

    Scenario: Removing products from the cart
        Given the user has an item in the cart
        When the user removes an item from the cart
        Then a new item is disappears from the cart