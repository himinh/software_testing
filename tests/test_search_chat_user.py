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

    # Init sidebar
    sidebar = Sidebar(self.driver)
    # self.driver.save_screenshot('_screenshots/home_page/home_page.png')

    # Navigate search Page
    sidebar.get_search_bar().click()
    sleep(2)

    # Init search page
    search_page = SearchPage(self.driver)

    # Enter search
    search_input = search_page.get_search_input()
    search_input.click()
    search_input.send_keys(SearchLocator().search_text)
    sleep(2)
    search_input.send_keys(Keys().ENTER)
    sleep(3)

    # Select user navigate to user profile
    user_1 = self.driver.find_element(by=By.CSS_SELECTOR, value=SearchLocator().user_minh_chiu)
    user_1.click()
    sleep(3)

    # Init profile page
    profile_page = ProfilePage(self.driver)

    # Toggle follow
    profile_page.get_follow_button().click()
    sleep(2)

    # Navigate message
    profile_page.get_message_button().click()
    sleep(3)

    # Init message page
    message_page = MessagePage(self.driver)
    input_text = message_page.get_input_text_box()
    input_text.click()
    input_text.send_keys("Hello Min!")
    sleep(2)
    input_text.send_keys(Keys().ENTER)
    sleep(3)

if __name__ == '__main__':
  unittest.main()
