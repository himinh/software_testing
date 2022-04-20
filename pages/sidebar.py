from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import SidebarLocator

class Sidebar():
  def __init__(self, driver):
    self.driver = driver

    self.search_link = driver.find_element(by=By.CSS_SELECTOR, value=SidebarLocator().search_link)
    self.logout_link = driver.find_element(by=By.CSS_SELECTOR, value=SidebarLocator().logout_link)

  def get_search_link(self):
    return self.search_link

  def get_logout_link(self):
    return self.logout_link

  def click_logout(self):
    self.logout_link.click()
