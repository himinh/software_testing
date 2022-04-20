from pages import LoginPage
from pages import HomePage
from locators import LoginLocator
from locators import ModalLocator
from WebDriverSetup import WebDriverSetup
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

invalid_email = 'minhad@gmail.com'
invalid_password = 'minh12323423'
valid_email = 'minh.mchiu@gmail.com'
valid_password = 'minh123123'

class TestLoginPage(WebDriverSetup):

  def test_uc1_login_page(self):
    self.driver.get(LoginLocator().login_page_url)
    login_page_title = "SignIn - SignUp"

    try:
      if self.driver.title == login_page_title:
        print("LoginPage loaded successfully")
        self.assertEqual(self.driver.title, login_page_title)
    except Exception as error:
      print(error+"LoginPage Failed to load")
    sleep(1)

    login_page = LoginPage(self.driver)
    login_heading = "Đăng nhập"

    self.assertEqual(login_page.get_login_heading().text, login_heading)
    sleep(1)


  def test_uc2_invalid_email(self):
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)

    # Enter values
    login_page.enter_login(invalid_email, valid_password)
    sleep(1)
    # Submit
    login_page.submit_login()
    sleep(1)

    # Check result
    error_label= self.driver.find_element(by=By.CSS_SELECTOR, value=LoginLocator().error_message)
    invalid_message = "Tên đăng nhập hoặc mật khẩu không chính xác."
    self.assertEqual(error_label.text, invalid_message)
    sleep(1)
    self.driver.save_screenshot('_screenshots/login_page/1.login_invalid_email.png')


  def test_uc3_invalid_password(self):
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)

    # Enter values
    login_page.enter_login(valid_email, invalid_password)
    sleep(1)

    # Submit
    login_page.submit_login()
    sleep(1)

    # Check result
    error_label= self.driver.find_element(by=By.CSS_SELECTOR, value=LoginLocator().error_message)
    invalid_message = "Tên đăng nhập hoặc mật khẩu không chính xác."
    self.assertEqual(error_label.text, invalid_message)
    sleep(1)
    self.driver.save_screenshot('_screenshots/login_page/2.login_invalid_password.png')


  def test_uc4_login_success(self):
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)

    # Enter values
    login_page.enter_login(valid_email, valid_password)
    sleep(1)

    # submit
    login_page.submit_login()
    sleep(1)
    self.driver.save_screenshot('_screenshots/login_page/3.login_success.png')

    home_page = HomePage(self.driver)
    # CLick logout
    home_page.logout()
    sleep(2)

    # Click confirm logout
    self.driver.find_element(by=By.XPATH, value=ModalLocator().confirm_logout).click()
    sleep(2)
    self.driver.save_screenshot('_screenshots/login_page/4.logout.png')


if __name__ == '__main__':
  unittest.main()
