Feature: Google Search click link and verify
  Scenario Outline: Click on the second visible link of google search
    Given I navigate to google.com
    When I typed "<search_term>" in the search box
    And click on the search button
    Then I click on the second visible link
    And verify that "<search_term>" is present on the page
    Examples:
      | search_term          |
      | Selenium with Python |
      | Selenium with Java   |