Feature: Login to SauceLabs

    As a common user
    I want to Login
    In order to have access to the application

    Scenario: Login with valid credentials
        Given the user is on SauceLabs page
        When the user logs in with valid credentials
        Then the user is redirected to the home of the application
