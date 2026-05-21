Feature: Home Page Functionality

    Scenario: User explores homepage

        Given user is on homepage
        When user scrolls homepage
        Then homepage should load successfully