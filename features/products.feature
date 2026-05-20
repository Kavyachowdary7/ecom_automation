Feature: Products Functionality

    Scenario: User explores products

        Given user is on homepage
        When user explores mobile products
        And user explores laptop products
        And user explores monitor products
        Then products should display successfully