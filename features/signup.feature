Feature: Signup Functionality

    Scenario: Successful signup

        Given user is on homepage
        When user clicks signup menu
        And user enters signup username
        And user enters signup password
        And user clicks signup button
        Then signup should be successful