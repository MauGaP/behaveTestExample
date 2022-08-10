Feature: Login Error

    As a user with invalid credentials
    I want to login to the application
    In order to validate the error message

    Scenario: Login with invalid credentials
        Given the user is on SauceLabs page
        When the user tries to log in with invalid credentials
        Then the user see the locked out user message