from pages import LoginAdminPage
from pages import Sidebar
from pages import AdminPage
from pages import AdminModal
import json

from locators import AdminModalLocator
from locators import AdminLocator


from WebDriverSetup import WebDriverSetup
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

valid_email = 'minh.mchiu@gmail.com'
valid_password = 'minh123123'
admin_url = 'https://social-network-awesome.herokuapp.com/admin'

first_name = 'user3'
last_name = 'new'
email = 'usernew3@gmail.com'
password = 'usernew123'

class TestAdminPage(WebDriverSetup):
  def test_uc10_create_new_user_success(self):
    self.driver.get(admin_url)

    # Login
    login_page = LoginAdminPage(self.driver)
    login_page.enter_login(valid_email, valid_password)
    sleep(2)
    login_page.submit_login()
    sleep(2)

    # Admin page
    admin_page = AdminPage(self.driver)
    admin_page.click_button_new_user()
    sleep(2)

    # Admin modal
    admin_modal = AdminModal(self.driver)
    self.driver.save_screenshot('_screenshots/admin_page/5.new_account_modal.png')

    # Enter info
    admin_modal.clear_form()
    role_text = AdminModalLocator().role_admin_text
    admin_modal.enter_new_account(first_name, last_name, email, password, role_text)
    self.driver.save_screenshot('_screenshots/admin_page/6.new_account_info.png')
    sleep(2)

    # submit
    admin_modal.submit_new_account()
    sleep(5)

    # Check new user
    new_user_str = self.driver.find_element(by=By.XPATH, value=AdminLocator().user_row_1).get_attribute('data-user')
    new_user = json.loads(new_user_str)

    self.assertEqual(new_user['firstName'], first_name)
    self.assertEqual(new_user['lastName'], last_name)
    self.assertEqual(new_user['email'], email)
    self.assertEqual(new_user['role'], role_text)

  def test_uc11_login_admin(self):
    self.driver.get(admin_url)

    # Login
    login_page = LoginAdminPage(self.driver)
    self.driver.save_screenshot('_screenshots/admin_page/1.admin_login_page.png')

    login_page.enter_login(email, password)
    self.driver.save_screenshot('_screenshots/admin_page/2.enter_login.png')
    sleep(2)
    login_page.submit_login()
    print("Login success!")
    sleep(5)

    admin_page = AdminPage(self.driver)
    self.driver.save_screenshot('_screenshots/admin_page/3.admin_page.png')
    admin_page.logout()
    sleep(2)
    self.driver.save_screenshot('_screenshots/admin_page/4.logout_success.png')

  def test_uc12_delete_created_user(self):
    self.driver.get(admin_url)

    # Login
    login_page = LoginAdminPage(self.driver)
    login_page.enter_login(valid_email, valid_password)
    sleep(2)
    login_page.submit_login()
    sleep(2)

    # Admin page
    admin_page = AdminPage(self.driver)

    # Get user row 1
    user_1_str = admin_page.get_data_user_row_1()

    # Click delete
    admin_page.click_button_delete_user()
    sleep(2)
    self.driver.save_screenshot('_screenshots/admin_page/6.new_account_info.png')

    # submit
    confirm_delete_user = self.driver.find_element(by=By.CSS_SELECTOR, value=AdminModalLocator().confirm_delete_user)
    confirm_delete_user.click()
    sleep(5)

    # Check user row 1
    new_user_str = self.driver.find_element(by=By.XPATH, value=AdminLocator().user_row_1).get_attribute('data-user')
    new_user = json.loads(new_user_str)
    user_1 = json.loads(user_1_str)
    self.assertNotEqual(new_user['email'], user_1['email'])

if __name__ == '__main__':
  unittest.main()
