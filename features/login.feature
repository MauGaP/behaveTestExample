#Feature: Log in
#
#  @smoke
#  @login
#  Scenario: Log in with valid credentials.
#    Given the browser is located on demoblaze.com
#    When the user enters his credentials on the login modal
#    Then the page displays the "Welcome <userName>" and the log out button on the header
#
#  @login
#  Scenario: Try to log in with invalid credentials.
#    Given the browser is located on demoblaze.com
#    When the user enters his credentials on the login modal
#    Then the page displays an alert modal with an unsuccessful message
