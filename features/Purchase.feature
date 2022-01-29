#Feature: Place order
#
#  @smoke
#  @bvt
#  @purchase
#  Scenario: Place order with one product in cart.
#    Given the browser is located on demoblaze.com
#    And the user already added a product to the cart
#    When the user navigates to cart
#    And places the order
#    Then the page displays a purchase confirmation modal
#
#  @purchase
#  Scenario: Place order with no product in cart.
#    Given the browser is located on demoblaze.com
#    When the user navigates to cart
#    And places the order
#    Then the page displays an error modal