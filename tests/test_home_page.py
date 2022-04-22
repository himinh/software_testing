from pages import LoginPage
from pages import HomePage

from locators import LoginLocator
from locators import HomeLocator
from locators import ModalLocator

from WebDriverSetup import WebDriverSetup
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

valid_email = 'minh.mchiu@gmail.com'
valid_password = 'minh123123'

class TestHomePage(WebDriverSetup):

  def test_uc5_create_post_success(self):
    # init login page
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)

    # enter login
    login_page.enter_login(valid_email, valid_password)
    sleep(1)

    # submit
    login_page.submit_login()
    sleep(1)


    # Init home page
    home_page = HomePage(self.driver)
    sleep(2)
    self.driver.save_screenshot('_screenshots/home_page/1.home_page.png')

    # Test 1: write post
    # Write post
    home_page.enter_post(HomeLocator().text_post)
    sleep(2)
    self.driver.save_screenshot('_screenshots/home_page/2.create_post_form.png')

    # Submit post
    home_page.submit_post()
    sleep(1)

    # Check posted post
    posted_text = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().posted_post).text
    self.assertEqual(posted_text, HomeLocator().text_post)
    self.driver.save_screenshot('_screenshots/home_page/3.post_created.png')
    # Bug 1: Thiếu chữ cái cuối
    # Fix:
    # self.assertEqual(posted_text, HomeLocator().text_post.strip())

    sleep(3)

  def test_uc6_like_post(self):
    # Login
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)
    login_page.enter_login(valid_email, valid_password)
    sleep(1)
    login_page.submit_login()
    sleep(1)

    # Init home page
    home_page = HomePage(self.driver)
    sleep(2)

    # Like post
    home_page.click_like_first_post()
    sleep(3)

    # Check liked post
    liked_class = 'post_button-container_content active'
    liked_button_element = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().container_like_first_post)
    current_liked_class = liked_button_element.get_attribute('class')
    self.assertEqual(current_liked_class, liked_class)
    self.driver.save_screenshot('_screenshots/home_page/4.post_liked.png')

  def test_usc7_pin_post(self):

    # Login
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)
    login_page.enter_login(valid_email, valid_password)
    sleep(1)
    login_page.submit_login()
    sleep(1)

    # Init home page
    home_page = HomePage(self.driver)
    sleep(2)

    # open pin post
    home_page.click_pin_post()
    sleep(1)
    self.driver.save_screenshot('_screenshots/home_page/5.pin_post_modal.png')

    # confirm pin
    confirm_pinned_post = self.driver.find_element(by=By.CSS_SELECTOR, value=ModalLocator().confirm_pinned)
    confirm_pinned_post.click()
    sleep(3)

    pinned_text = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().pined_text).text
    self.assertIsNotNone(pinned_text)

  def test_usc8_delete_post(self):

    # Login
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)
    login_page.enter_login(valid_email, valid_password)
    sleep(1)
    login_page.submit_login()
    sleep(1)

    # Init home page
    home_page = HomePage(self.driver)
    sleep(2)

    # Get first post
    first_post_id = home_page.get_first_post().get_attribute('data-id')

    # Open modal delete post
    home_page.click_delete_post()
    self.driver.save_screenshot('_screenshots/home_page/6.delete_post_modal.png')
    sleep(2)

    # confirm delete
    confirm_delete = self.driver.find_element(by=By.CSS_SELECTOR, value=ModalLocator().confirm_deleted_post)
    confirm_delete.click()
    sleep(3)

    # Check deleted post
    first_post = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().first_post)
    self.assertNotEqual(first_post_id, first_post.get_attribute('data-id'))
    sleep(3)

if __name__ == '__main__':
  unittest.main()
