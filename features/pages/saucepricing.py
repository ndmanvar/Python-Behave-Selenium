from pages.page import Page

class SaucePricing(Page):
  """
  SaucePricing class that represents the Sauce Labs pricing page
  """
  def __init__(self, selenium_driver):
    Page.__init__(self, selenium_driver, 'https://saucelabs.com/pricing')

  def get_pricing_plans(self):
    plans = {}
    pricing_plans = self.driver.find_elements_by_css_selector(".column.year")

    for element in pricing_plans:
      level = element.find_element_by_css_selector(".level").text
      cost = element.find_element_by_css_selector(".cost").text
      plans[level] = cost 
    return plans 