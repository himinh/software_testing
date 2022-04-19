from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import SidebarLocator

class Sidebar():
  def __init__(self, driver):
    self.driver = driver

    self.search_bar = driver.find_element(by=By.CSS_SELECTOR, value=SidebarLocator().search_bar)

  def get_search_bar(self):
    return self.search_bar
