Feature: Log in

  @smoke @login
  Scenario Outline: Log in with valid credentials.
    Given the <browser> browser is located on demoblaze.com
    When the user enters his <username> and <password> credentials on the login modal
    Then the page displays the "Welcome <username>" and the log out button on the header
    Examples:
      | browser | username | password |
      | chrome  | MauGaP   | 123456   |

  @login
  Scenario Outline: Try to log in with invalid credentials.
    Given the <browser> browser is located on demoblaze.com
    When the user enters his <username> and <password> credentials on the login modal
    Then the page displays an alert with an unsuccessful login message
    Examples:
      | browser | username        | password |
      | chrome  | invalidUsername | 123456   |