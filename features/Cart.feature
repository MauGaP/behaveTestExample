#Feature: Cart
#
#  @smoke
#  @cart
#  Scenario: Login, add product to cart
#    Given the browser is located on demoblaze.com
#    And the user is already logged in
#    When the user filters phones
#    And selects the first product
#    And adds the product to the cart
#    Then the page displays a confirmation message alert
#
#  @cart
#  Scenario: Login, add a product to cart and delete the product from cart
#    Given the browser is located on demoblaze.com
#    And the user already added one product to the cart
#    When the user delete the product from the cart
#    Then the page displays an empty cart