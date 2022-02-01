Feature: Product store

  @smoke @product_store
  Scenario Outline: Login and apply a filter.
    Given the <browser> browser is located on demoblaze.com
    And an existing user is already logged in
    When the user filters <category>
    Then the page only displays <category> items
    Examples:
      | browser | category |
      | chrome  | monitors |
      | chrome  | phones   |
      | chrome  | laptops  |
      | firefox | default |

  @bvt @smoke @product_store
  Scenario Outline: Login, apply a filter and open the first product
    Given the <browser> browser is located on demoblaze.com
    And an existing user is already logged in
    When the user filters <category>
    And selects the first product in <category>
    Then the page displays all the information correctly for the first item in <category>
    Examples:
      | browser | category |
      | chrome  | phones   |
