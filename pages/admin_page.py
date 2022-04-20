from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import AdminLocator

class AdminPage():
  def __init__(self, driver):
    self.driver = driver

    self.button_new_user = driver.find_element(by=By.CSS_SELECTOR, value=AdminLocator().button_new_user)
    self.button_logout = driver.find_element(by=By.CSS_SELECTOR, value=AdminLocator().button_logout)
    self.user_row_1 = driver.find_element(by=By.XPATH, value=AdminLocator().user_row_1)
    self.delete_user_row_1 = driver.find_element(by=By.XPATH, value=AdminLocator().delete_user_row_1)

  def click_button_delete_user(self):
    self.delete_user_row_1.click()

  def click_button_new_user(self):
    self.button_new_user.click()

  def get_data_user_row_1(self):
    return self.user_row_1.get_attribute('data-user')

  def logout(self):
    self.button_logout.click()

  def get_button_new_user(self):
    return self.button_new_user
