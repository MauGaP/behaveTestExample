Feature: Log out

  @smoke @logout
  Scenario Outline: As a logged in user, log out.
    Given the <browser> browser is located on demoblaze.com
    And an existing user is already logged in
    When the user tries to logout
    Then "login" and "sign up" buttons are displayed on the page
    Examples:
      | browser |
      | chrome  |
