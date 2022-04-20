from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import LoginLocator

class LoginPage():
  def __init__(self, driver):
    self.driver = driver
    self.login_heading = driver.find_element(by=By.CSS_SELECTOR, value=LoginLocator().heading_text)
    self.login_email = driver.find_element(by=By.CSS_SELECTOR, value=LoginLocator().email)
    self.login_password = driver.find_element(by=By.CSS_SELECTOR, value=LoginLocator().password)
    self.submit_button = driver.find_element(by=By.CSS_SELECTOR, value=LoginLocator().submit)

  def get_login_heading(self):
    return self.login_heading

  def get_login_email(self):
    return self.login_email

  def get_login_password(self):
    return self.login_password

  def get_submit_button(self):
    return self.submit_button

  def get_error_label(self):
    return self.driver

  def enter_login(self, email, password):
    self.login_email.send_keys(email)
    self.login_password.send_keys(password)

  def clear_form(self):
    self.login_email.clear()
    self.login_password.clear()

  def submit_login(self):
    self.submit_button.click()
