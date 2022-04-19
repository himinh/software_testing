from pages import LoginPage
from locators import LoginLocator
from WebDriverSetup import WebDriverSetup
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

invalid_email = 'minhad@gmail.com'
invalid_password = 'minh123'
valid_email = 'minh.mchiu@gmail.com'
valid_password = 'minh123123'

class TestLoginPage(WebDriverSetup):

  # def test_uc1_login_page(self):
  #   self.driver.get(LoginLocator().login_page_url)
  #   login_page_title = "SignIn - SignUp"

  #   try:
  #     if self.driver.title == login_page_title:
  #       print("LoginPage loaded successfully")
  #       self.assertEqual(self.driver.title, login_page_title)
  #   except Exception as error:
  #     print(error+"LoginPage Failed to load")
  #   sleep(1)

  #   login_page = LoginPage(self.driver)
  #   login_heading = "Đăng nhập"

  #   self.assertEqual(login_page.get_login_heading().text, login_heading)
  #   sleep(1)


  def test_uc2_invalid_email(self):
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)

    # enter email
    email_input = login_page.get_login_email()
    email_input.send_keys(invalid_email)
    sleep(1)

    # enter password
    password_input = login_page.get_login_password()
    password_input.send_keys(valid_password)
    sleep(1)

    # submit
    submit_button = login_page.get_submit_button()
    submit_button.click()
    sleep(1)

    # Check result
    error_label= self.driver.find_element(by=By.CSS_SELECTOR, value=LoginLocator().error_message)
    invalid_message = "Tên đăng nhập hoặc mật khẩu không chính xác."
    self.assertEqual(error_label.text, invalid_message)
    sleep(1)


  def test_uc3_invalid_password(self):
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)

    # enter email
    email_input = login_page.get_login_email()
    email_input.send_keys(invalid_email)
    sleep(2)

    # enter password
    password_input = login_page.get_login_password()
    password_input.send_keys(valid_password)
    sleep(2)

    # submit
    submit_button = login_page.get_submit_button()
    submit_button.click()
    sleep(1)

    # Check result
    error_label= self.driver.find_element(by=By.CSS_SELECTOR, value=LoginLocator().error_message)
    invalid_message = "Tên đăng nhập hoặc mật khẩu không chính xác."
    self.assertEqual(error_label.text, invalid_message)
    sleep(1)


if __name__ == '__main__':
  unittest.main()
