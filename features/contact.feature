Feature: Contact Functionality

    Scenario: Send contact message

        Given user clicks contact menu
        When user enters contact email
        And user enters registered contact name
        And user enters message
        And user clicks send message button
        Then contact message should be sent successfully