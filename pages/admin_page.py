from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import AdminLocator

class AdminPage():
  def __init__(self, driver):
    self.driver = driver

    self.button_new_user = driver.find_element(by=By.CSS_SELECTOR, value=AdminLocator().button_new_user)
    self.button_logout = driver.find_element(by=By.CSS_SELECTOR, value=AdminLocator().button_logout)

  def click_button_new_user(self):
    self.button_new_user.click()

  def logout(self):
    self.button_logout.click()

  def get_button_new_user(self):
    return self.button_new_user
