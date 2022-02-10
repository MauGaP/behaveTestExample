Feature: Log in

  Background:
    Given the user opens the page demoblaze.com in chrome browser

  @smoke @login
  Scenario Outline: Log in with valid credentials.
    When the user enters his <username> and <password> credentials on the login modal
    Then the page displays the "Welcome <username>" and the log out button on the header
    Examples:
      | username | password |
      | MauGaP   | 123456   |

  @login
  Scenario Outline: Try to log in with invalid credentials.
    When the user enters his <username> and <password> credentials on the login modal
    Then the page displays an alert with an unsuccessful login message
    Examples:
      | username        | password |
      | invalidUsername | 123456   |
