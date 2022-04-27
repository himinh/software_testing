from pages import RegisterPage
from pages import LoginPage
from locators import GmailLocator
from locators import RegisterLocator

from WebDriverSetup import WebDriverSetup
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

first_name = 'Hello'
last_name = 'hi'
email = 'minhhihi@gmail.com'
password = 'minh123123'

class TestRegisterPage(WebDriverSetup):

  def test_uc01_register_invalid_firstName(self):
    self.driver.get(RegisterLocator().page_url)
    sleep(2)
    self.driver.find_element(by=By.XPATH, value=RegisterLocator().xpath_sign_up_btn).click()
    sleep(1)

    register_page = RegisterPage(self.driver)

    # Enter login
    register_page.enter_register("", last_name, email, password)
    sleep(1)
    register_page.submit_register()
    sleep(2)

    # Validate
    error_message = "firstName is a required field"
    error_message_label = self.driver.find_element(by=By.CSS_SELECTOR, value=RegisterLocator().error_message)
    self.assertEqual(error_message, error_message_label.text)
    sleep(1)


  def test_uc02_register_success(self):
    self.driver.get(RegisterLocator().page_url)
    sleep(2)
    self.driver.find_element(by=By.XPATH, value=RegisterLocator().xpath_sign_up_btn).click()

    register_page = RegisterPage(self.driver)

    # Enter login
    register_page.enter_register(first_name, last_name, email, password)
    sleep(1)
    register_page.submit_register()
    sleep(2)

    # Validate
    success_message = "Tài khoản "+email+" đã được tạo, vui lòng kiểm tra email của bạn để active tài khoản trước khi đăng nhập."
    success_message_label = self.driver.find_element(by=By.CSS_SELECTOR, value='.alert.alert-success .message')
    self.assertEqual(success_message, success_message_label.text)
    sleep(1)


  def test_uc03_login_invalid_verify_email(self):
    self.driver.get(RegisterLocator().page_url)
    login_page = LoginPage(self.driver)

    # Enter values
    login_page.enter_login(email, password)
    sleep(1)

    # submit
    login_page.submit_login()
    sleep(2)

    error_message = 'Email đã đăng ký nhưng chưa active tài khoản, vui lòng kiểm tra email của bạn hoặc liên hệ với bộ phận hỗ trợ của chúng tôi.'
    error_message_label = self.driver.find_element(by=By.CSS_SELECTOR, value=RegisterLocator().error_message)
    self.assertEqual(error_message, error_message_label.text)


if __name__ == '__main__':
  unittest.main()
