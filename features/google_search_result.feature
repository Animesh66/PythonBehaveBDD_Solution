Feature: Search click
  Scenario Outline: Click on the second visible link of google search
    Given I navigate to google.com
    When I typed "<search_term>" in the searchbox
    And click on the search button
    Then I click on the second visible link
    And verify that search term is present on the page
    Examples:
      | search_term          |
      | Selenium with Python |
      | Selenium with Java   |