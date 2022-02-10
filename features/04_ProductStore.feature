Feature: Product store

  Background:
    Given the user opens the page demoblaze.com in chrome browser

  @smoke @product_store
  Scenario Outline: Login and apply a filter.
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
    And an existing user is already logged in
    When the user filters <category>
    And selects the first product displayed
    Then the page displays all the information correctly for the first item in <category>
    Examples:
      | category |
      | phones   |
