Feature: logout

Scenario: logout

    Given the user is on inventory page
    When the user logs out
    Then the user is redirected to login page