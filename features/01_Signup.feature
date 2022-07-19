Feature: Sign up

  Background:
    Given the user opens the page demoblaze.com in chrome browser

  @smoke @signup
  Scenario Outline: Register a new user
    When the user registers his <user> and <password> credentials on the sign up modal
    Then the page displays an alert with a successful confirmation message
    Examples:
    # In a more robust system or one that I have access to the user registration database, I would create an script or
    # method to delete stored users. Since I can't do this here, I imported the uuid class and called uuid4() when the
    # user is not registered
      | user             | password |
      | unregisteredUser | 12345    |

  @signup
  Scenario Outline: Register a user already registered
    When the user registers his <user> and <password> credentials on the sign up modal
    Then the page displays an alert with an unsuccessful signup message
    Examples:
      | user           | password |
      | registeredUser | 12345    |

  Scenario: user logs in successfully
    Given the user is on login page
    When The user enters valid credentials
    Then He is redirected to his account
    And He is successfully logged in
