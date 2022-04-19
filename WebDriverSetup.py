import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import warnings
import urllib3

class WebDriverSetup(unittest.TestCase):
  def setUp(self):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()

  # def tearDown(self):
    # if (self.driver != None):
      # print("Cleanup of test environment")
      # self.driver.close()
      # self.driver.quit()
