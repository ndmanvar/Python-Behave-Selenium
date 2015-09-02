from pages.page import Page

class SauceMain(Page):
  """
  SauceMain class that represents the Sauce Labs main page
  """
  def __init__(self, selenium_driver):
    Page.__init__(self, selenium_driver, 'https://saucelabs.com/')

  def find_pricing_link(self):
    return self.driver.find_element_by_link_text("PRICING")
    