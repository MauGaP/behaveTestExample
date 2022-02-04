Feature: Sign up

  @smoke @signup
  Scenario Outline: Register a new user
    Given the user opens the page demoblaze.com in chrome browser.
    When the user registers his <user> and <password> credentials on the sign up modal
    Then the page displays an alert with a successful confirmation message
    Examples:
    # In a more robust system or one that I have access to the user registration database, I would create an script or
    # method to delete stored users. Since I can't do this here, please change the name of the user in this example
    # in order to test it properly
      | user             | password |
      | unregisteredUser | 12345    |

  @signup
  Scenario Outline: Register a user already registered
    Given the user opens the page demoblaze.com in chrome browser.
    When the user registers his <user> and <password> credentials on the sign up modal
    Then the page displays an alert with an unsuccessful signup message
    Examples:
      | user           | password |
      | registeredUser | 12345    |