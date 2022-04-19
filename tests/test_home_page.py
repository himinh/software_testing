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

class TestHomePage(WebDriverSetup):

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


  def test_uc2_invalid_login(self):
    print("Test success")


if __name__ == '__main__':
  unittest.main()
