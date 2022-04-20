from pages import LoginPage
from pages import Sidebar
from pages import SearchPage
from pages import ProfilePage
from pages import MessagePage

from locators import LoginLocator
from locators import SearchLocator
from locators import ProfileLocator
from locators import MessageLocator


from WebDriverSetup import WebDriverSetup
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

valid_email = 'minh.mchiu@gmail.com'
valid_password = 'minh123123'

class TestSearchChatUser(WebDriverSetup):
  def test_uc5_create_post_success(self):
    self.driver.get(LoginLocator().login_page_url)

    # Login
    login_page = LoginPage(self.driver)
    login_page.enter_login(valid_email, valid_password)
    sleep(1)
    login_page.submit_login()
    sleep(2)


    # Navigate search page
    sidebar = Sidebar(self.driver)
    sidebar.click_search_link()
    sleep(2)

    # Search
    search_page = SearchPage(self.driver)
    search_page.enter_search('minh')
    sleep(2)
    self.driver.save_screenshot('_screenshots/search_page/1.search_name_minh.png')

    search_page.submit_search()
    sleep(3)
    self.driver.save_screenshot('_screenshots/search_page/2.result_search_name_minh.png')


    # Select user navigate to user profile
    user_1 = self.driver.find_element(by=By.CSS_SELECTOR, value=SearchLocator().user_minh_chiu)
    user_1.click()
    sleep(3)

    # Profile page
    profile_page = ProfilePage(self.driver)
    self.driver.save_screenshot('_screenshots/search_page/3.profile_page.png')

    # toggle follow
    profile_page.click_follow_button()
    sleep(2)
    self.driver.save_screenshot('_screenshots/search_page/4.toggle_follow.png')

    # navigate message
    profile_page.click_message_button()
    sleep(3)

    # Init message page
    message_page = MessagePage(self.driver)
    self.driver.save_screenshot('_screenshots/search_page/2.message_page.png')

    message_page.enter_message('Hello Min!')
    sleep(2)
    self.driver.save_screenshot('_screenshots/search_page/6.enter_message.png')
    message_page.submit_message()
    sleep(4)
    self.driver.save_screenshot('_screenshots/search_page/7.send_message_success.png')

if __name__ == '__main__':
  unittest.main()
