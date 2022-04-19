from pages import LoginPage
from pages import HomePage
from locators import LoginLocator
from locators import HomeLocator
from WebDriverSetup import WebDriverSetup
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

valid_email = 'minh.mchiu@gmail.com'
valid_password = 'minh123123'

class TestHomePage(WebDriverSetup):
  def test_uc5_create_post_success(self):
    self.driver.get(LoginLocator().login_page_url)
    login_page = LoginPage(self.driver)

    # enter email
    email_input = login_page.get_login_email()
    email_input.send_keys(valid_email)
    sleep(1)

    # enter password
    password_input = login_page.get_login_password()
    password_input.send_keys(valid_password)
    sleep(1)

    # submit
    submit_button = login_page.get_submit_button()
    submit_button.click()
    sleep(1)

    home_page = HomePage(self.driver)
    sleep(2)
    self.driver.save_screenshot('_screenshots/home_page/1.home_page.png')

    # Open modal create post form
    home_page.get_textarea_button().click()
    sleep(1)

    # Enter text
    textarea = home_page.get_textarea_post()
    textarea.click()
    textarea.send_keys(HomeLocator().create_text_post)
    sleep(1)
    self.driver.save_screenshot('_screenshots/home_page/2.create_post_form.png')

    # Submit create
    home_page.get_submit_create_post().click()
    sleep(4)

    posted_text = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().posted_text).text
    self.assertEqual(posted_text, HomeLocator().create_text_post.strip())
    self.driver.save_screenshot('_screenshots/home_page/3.post_created.png')
    # Bug 1: Thiếu chữ cái cuối

    posted_post = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().first_post)
    posted_post_id = posted_post.get_attribute('data-id')


    # Like post
    self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().like_first_post).click()
    sleep(3)

    liked_class = 'post_button-container_content active'
    liked_button_element = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().liked_first_post_active)
    current_like_class = liked_button_element.get_attribute('class')
    self.assertEqual(current_like_class, liked_class)
    self.driver.save_screenshot('_screenshots/home_page/4.post_liked.png')

    # open pin post
    self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().pin_first_post).click()
    sleep(1)
    self.driver.save_screenshot('_screenshots/home_page/5.pin_post_modal.png')

    # confirm pin
    confirm_pinned_post = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().confirm_pinned_post)
    confirm_pinned_post.click()
    sleep(3)

    pinned_text = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().pined_text).text
    self.assertIsNotNone(pinned_text)


    # Delete post
    delete_pin_post = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().delete_first_post)
    delete_pin_post.click()
    self.driver.save_screenshot('_screenshots/home_page/6.delete_post_modal.png')
    sleep(2)

    # confirm delete
    submit_delete = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().confirm_deleted_post)
    submit_delete.click()
    sleep(3)


    # Check deleted post
    first_post = self.driver.find_element(by=By.CSS_SELECTOR, value=HomeLocator().first_post)
    self.assertNotEqual(posted_post_id, first_post.get_attribute('data-id'))
    sleep(3)


if __name__ == '__main__':
  unittest.main()
