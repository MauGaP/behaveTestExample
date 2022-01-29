#Feature: Log out
#
#  @smoke
#  @logout
#  Scenario: As a logged in user, log out.
#    Given the browser is located on demoblaze.com
#    And the user is already logged in
#    When the user tries to logout
#    Then the user is logged out
#    And "login" and "sign up" buttons are displayed on the page
