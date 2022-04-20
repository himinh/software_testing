from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.home_locator import HomeLocator
from pages.sidebar import Sidebar

class HomePage():
  def __init__(self, driver):
    self.driver = driver

    self.textarea_button = driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().textarea_button)
    self.textarea_post = driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().textarea_post)
    self.submit_create_post = driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().submit_create_post)
    self.like_first_post = driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().like_first_post)
    self.pin_first_post = driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().pin_first_post)

  def get_textarea_button(self):
    return self.textarea_button

  def get_textarea_post(self):
    return self.textarea_post

  def get_submit_create_post(self):
    return self.submit_create_post

  def get_like_first_post(self):
    return self.like_first_post

  def get_pin_first_post(self):
    return self.pin_first_post

  def logout(self):
    sidebar = Sidebar(self.driver)
    sidebar.click_logout()
