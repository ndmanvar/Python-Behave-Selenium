Feature: Manipulating the guinea pig test website

  Scenario Outline: We want to check the first box and populate the email field
    Given we are also on "<platform>" using "<browser_name>" version "<version>"
      And we are looking at the guinea pig website
    When we click on the uncheck box
    Then it should be checked

    When I populate the email field 
    Then it should contain the value I entered

    Examples: Platforms
      | platform    | browser_name      | version |
      | Windows 8.1 | internet explorer | 11.0    |
      | OS X 10.8   | chrome            | 44.0    |
      | OS X 10.10  | safari            | 8.0     |
      | OS X 10.11  | firefox           | 40.0    |

  Scenario Outline: We want to click on the link and verify it takes us to a new page
    Given we use "<platform>" and "<browser_name>" version "<version>"
      And we are on the guinea pig website
    When I click on the link
    Then I should see a new page  

    Examples: Platforms
      | platform    | browser_name      | version |
      | Windows 8.1 | internet explorer | 11.0    |
      | OS X 10.8   | chrome            | 44.0    |
      | OS X 10.10  | safari            | 8.0     |
      | OS X 10.11  | firefox           | 40.0    |


