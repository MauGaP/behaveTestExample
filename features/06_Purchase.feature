Feature: Place order

  @smoke
  @bvt
  @purchase
  Scenario: Place order with one product in cart.
    Given the user opens the page demoblaze.com in chrome browser
    And the user already added one product to the cart
    When the user places the order
    Then the page displays a purchase confirmation modal

  @purchase
  Scenario: Place order with no product in cart.
    Given the user opens the page demoblaze.com in chrome browser
    When the user places the order
    Then the page displays an error modal
