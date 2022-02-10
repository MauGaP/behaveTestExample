Feature: Cart

  Background:
    Given the user opens the page demoblaze.com in chrome browser

  @smoke @cart
  Scenario Outline: Login, add product to cart
    Given an existing user is already logged in
    When the user filters <category>
    And selects the first product displayed
    And adds the product to the cart
    Then the page displays a confirmation message alert
    Examples:
      | category |
      | phones   |

  @cart
  Scenario: Login, add a product to cart and delete the product from cart
    Given the user already added one product to the cart
    When the user deletes the product from the cart
    Then the page displays an empty cart
