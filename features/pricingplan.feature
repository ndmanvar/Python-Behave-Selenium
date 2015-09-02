Feature: Verify the individual price plan

  Scenario Outline: We want to see that the individual plan is present and it costs $49
    Given we are on "<platform>" using "<browser_name>" version "<version>"
      And we are looking at the sauce labs website
    When we click on the pricing link
    When we see the individual plan present
    Then we should verify the price is $49/month

    Examples: Platforms
      | platform    | browser_name      | version |
      | Windows 8.1 | internet explorer | 11.0    |
      | OS X 10.8   | chrome            | 44.0    |
      | OS X 10.10  | safari            | 8.0     |
      | OS X 10.11  | firefox           | 40.0    |