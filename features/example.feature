@test
Feature: Google Search
  As a user
  I want to search for information on Google
  So that I can find relevant results

  Scenario: Search for "Selenium Python"
    Given I open the Google homepage
    When I search for "Selenium Python"
    Then I should see results containing "Selenium Python"
