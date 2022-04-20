from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import MessageLocator

class MessagePage():
  def __init__(self, driver):
    self.driver = driver
    self.input_text_box = driver.find_element(by=By.CSS_SELECTOR, value=MessageLocator().input_text_box)


  def enter_message(self, text):
    self.input_text_box.click()
    self.input_text_box.send_keys(text)

  def submit_message(self):
    self.input_text_box.send_keys(Keys().ENTER)

  def get_input_text_box(self):
    return self.input_text_box
