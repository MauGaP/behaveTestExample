#Feature: Product store
#
#  @smoke
#  @product_store
#  Scenario: Login and apply a filter.
#    Given the browser is located on demoblaze.com
#    And the user is already logged in
#    When the user filters monitors
#    Then the page only displays monitors
#
#  @bvt
#  @smoke
#  @product_store
#  Scenario: Login, apply a filter and open the first product
#    Given the browser is located on demoblaze.com
#    And the user is already logged in
#    When the user filters phones
#    And selects the first product
#    Then the page displays all its information correctly
