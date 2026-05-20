Feature: Cart Functionality

    Scenario: Add product to cart

        Given user selects laptop category
        When user selects laptop product
        And user clicks add to cart
        And user accepts cart alert
        And user opens cart page
        Then product should be added to cart