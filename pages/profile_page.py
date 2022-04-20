from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import ProfileLocator

class ProfilePage():
  def __init__(self, driver):
    self.driver = driver

    self.message_button = driver.find_element(by=By.CSS_SELECTOR, value=ProfileLocator().message_button)
    self.follow_button = driver.find_element(by=By.CSS_SELECTOR, value=ProfileLocator().follow_button)

  def click_message_button(self):
    self.message_button.click()

  def click_follow_button(self):
    self.follow_button.click()

  def get_message_button(self):
    return self.message_button

  def get_follow_button(self):
    return self.follow_button
