Feature: Checkout Functionality

    Scenario: Complete checkout process

        Given product is already added to cart
        When user clicks place order
        And user enters checkout username
        And user enters country "India"
        And user enters city "Chennai"
        And user enters card "123456"
        And user enters month "May"
        And user enters year "2026"
        And user clicks purchase button
        Then order should be placed successfully