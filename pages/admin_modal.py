from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from locators import AdminModalLocator

class AdminModal():
  def __init__(self, driver):
    self.driver = driver

    self.first_name_input = driver.find_element(by=By.CSS_SELECTOR, value=AdminModalLocator().first_name_input)
    self.last_name_input = driver.find_element(by=By.CSS_SELECTOR, value=AdminModalLocator().last_name_input)
    self.email_input = driver.find_element(by=By.CSS_SELECTOR, value=AdminModalLocator().email_input)
    self.password_input = driver.find_element(by=By.CSS_SELECTOR, value=AdminModalLocator().password_input)
    self.role_select = driver.find_element(by=By.CSS_SELECTOR, value=AdminModalLocator().role_select)
    self.submit_created = driver.find_element(by=By.CSS_SELECTOR, value=AdminModalLocator().submit_created)

  def enter_new_account(self, first_name, last_name, email, password, role_text):
    self.enter_first_name(first_name)
    self.enter_last_name(last_name)
    self.enter_email(email)
    self.enter_password(password)
    self.select_role(role_text)

  def clear_form(self):
    self.first_name_input.clear()
    self.last_name_input.clear()
    self.email_input.clear()
    self.password_input.clear()

  def submit_new_account(self):
    self.submit_created.click()

  def enter_first_name(self, first_name):
    self.first_name_input.click()
    self.first_name_input.send_keys(first_name)
    sleep(1)

  def enter_last_name(self, last_name):
    self.last_name_input.click()
    self.last_name_input.send_keys(last_name)
    sleep(1)

  def enter_email(self, email):
    self.email_input.click()
    self.email_input.send_keys(email)
    sleep(1)

  def enter_password(self, password):
    self.password_input.click()
    self.password_input.send_keys(password)
    sleep(1)

  def select_role(self, role_text):
    select = Select(self.role_select)
    select.select_by_visible_text(role_text)
