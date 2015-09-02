import os
import time
from selenium import webdriver

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
assert username, "Unable to pull username from environment variables"
assert access_key, "Unable to pull access_key from environment variables"

build = int(time.time());

def make_browser(name, platform, browser_name, version):
  desired_cap = {
      "name": name,
      "platform": platform,
      "browser_name": browser_name,
      "version": version,
      "build": build,
  }
  browser = webdriver.Remote(
  command_executor ='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key),
  desired_capabilities = desired_cap)
  return browser







