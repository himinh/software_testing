from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import SearchLocator

class SearchPage():
  def __init__(self, driver):
    self.driver = driver
    self.search_input = driver.find_element(by=By.CSS_SELECTOR, value=SearchLocator().search_input)


  def enter_search(self, text):
    self.search_input.click()
    self.search_input.send_keys(text)

  def submit_search(self):
    self.search_input.send_keys(Keys().RETURN)

  def get_search_input(self):
    return self.search_input
