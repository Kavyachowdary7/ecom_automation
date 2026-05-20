Feature: Login Functionality

    Scenario: Successful login

        Given user is on homepage
        When user clicks login menu
        And user enters login username
        And user enters login password
        And user clicks login button
        Then user should login successfully