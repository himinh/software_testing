from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import RegisterLocator


class RegisterPage():
  def __init__(self, driver):
    self.driver = driver
    self.first_name_input = driver.find_element(by=By.CSS_SELECTOR, value=RegisterLocator().first_name_input)
    self.last_name_input = driver.find_element(by=By.CSS_SELECTOR, value=RegisterLocator().last_name_input)
    self.email_input = driver.find_element(by=By.CSS_SELECTOR, value=RegisterLocator().email_input)
    self.password_input = driver.find_element(by=By.CSS_SELECTOR, value=RegisterLocator().password_input)
    self.submit_btn = driver.find_element(by=By.XPATH, value=RegisterLocator().submit_btn)

  def enter_register(self, first_name, last_name, email, password):
    self.first_name_input.send_keys(first_name)
    self.last_name_input.send_keys(last_name)
    sleep(1)
    self.email_input.send_keys(email)
    sleep(1)
    self.password_input.send_keys(password)
    sleep(1)


  def clear_form(self):
    self.first_name_input.clear()
    self.last_name_input.clear()
    self.email_input.clear()
    self.password_input.clear()

  def submit_register(self):
    self.submit_btn.click()
