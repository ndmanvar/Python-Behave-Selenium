from pages.page import Page

class SauceGuineaPig2(Page):
  """
  SauceGuineaPig class that represents page 2 of the guienea pig website
  """
  def __init__(self, selenium_driver):
    Page.__init__(self, selenium_driver, 'https://saucelabs.com/test-guinea-pig2.html')


