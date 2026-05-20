Feature: Home Page Functionality

    Scenario: User explores homepage

        Given user is on homepage
        When user scrolls homepage
        And user clicks next banner
        And user clicks previous banner
        Then homepage should load successfully