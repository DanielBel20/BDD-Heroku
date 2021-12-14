Feature: Add delete button on page
  As a user,
  I want to check if when I click on Add Element button,
  The Delete button appears


    Scenario: Click Add Element on heroku add remove elements page
        Given the Heroku add remove elements page is displayed
        When the user click on Add Element button
        Then the delete button will be displayed
