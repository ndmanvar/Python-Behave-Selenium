from selenium import webdriver
from pages.saucemain import SauceMain
from pages.saucepricing import SaucePricing
from features.browser.browsers import make_browser

@given('we are on "{platform}" using "{browser_name}" version "{version}"')
def step_impl(context, platform, browser_name, version):
  context.browser = make_browser(context.name, platform, browser_name, version)

@given('we are looking at the sauce labs website')
def step_impl(context):
  context.page = SauceMain(context.browser)

@when('we click on the pricing link')
def step_impl(context):
  context.page.find_pricing_link().click()
  context.page = SaucePricing(context.browser)
  assert "Pricing" in context.page.get_title(), "Couldn't find 'Pricing' in the title"

@when('we see the individual plan present')
def step_impl(context):
  assert "Individual" in context.page.get_pricing_plans(), "Couldn't find Individual in Plans"

@then('we should verify the price is $49/month')
def step_impl(context):
  plans = context.page.get_pricing_plans()
  assert plans['Individual'] == '$49/month', "Price of $49/month not found"





