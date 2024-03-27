Feature: Login
  Identify the visitor and store their data

  Scenario: Successful Login
    Given username and pwd password
    When Log In button clicked
    Then show welcome message
