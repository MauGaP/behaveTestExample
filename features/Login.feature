Feature: Log in

  @smoke @login
  Scenario Outline: Log in with valid credentials.
    Given the chrome browser is located on demoblaze.com
    When the user enters his username and password credentials on the login modal
    Then the page displays the "Welcome <userName>" and the log out button on the header
    Examples:
    | username   | password  |
    | testUser1  | 123456    |

  @login
  Scenario Outline: Try to log in with invalid credentials.
    Given the chrome browser is located on demoblaze.com
    When the user enters his credentials on the login modal
    Then the page displays an alert modal with an unsuccessful login message
    Examples:
    | username        | password  |
    | invalidUsername | 123456    |