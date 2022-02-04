Feature: Product store

  @smoke @product_store
  Scenario Outline: Login and apply a filter.
    Given the user opens the page demoblaze.com in chrome browser.
    And an existing user is already logged in
    When the user filters <category>
    Then the page only displays <category> items
    Examples:
      | category |
      | monitors |
      | phones   |
      | laptops  |
      | default  |

  @bvt @smoke @product_store
  Scenario Outline: Login, apply a filter and open the first product
    Given the user opens the page demoblaze.com in chrome browser.
    And an existing user is already logged in
    When the user filters <category>
    And selects the first product displayed
    Then the page displays all the information correctly for the first item in <category>
    Examples:
      | category |
      | phones   |
