Feature: Log out

  Background:
    Given the user opens the page demoblaze.com in chrome browser

  @smoke @logout
  Scenario: As a logged in user, log out.
    And an existing user is already logged in
    When the user tries to logout
    Then "login" and "sign up" buttons are displayed on the page
