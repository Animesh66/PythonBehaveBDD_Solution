Feature: Search click
  Scenario: Click on the second visible link of google search
    Given I navigate to google.com
    When I typed "Selenium with Python" in the searchbox
    And click on the search button
    Then I click on the second visible link
    And verify that search term is present on the page