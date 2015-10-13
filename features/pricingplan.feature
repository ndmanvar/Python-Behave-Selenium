Feature: Verify the individual price plan

  Scenario: We want to see that the individual plan is present and it costs $49
    Given we are looking at the sauce labs website
    When we click on the pricing link
    When we see the individual plan present
    Then we should verify the price is $49/month
