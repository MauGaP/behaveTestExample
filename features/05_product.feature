Feature: Identify a product

    As a common user
    I want to select a product
    In order to see its information

    Scenario: View product information
        Given the user is on inventory page
        When the user select a product
        Then information about the product is displayed