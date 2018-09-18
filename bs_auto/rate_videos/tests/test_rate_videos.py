from selenium import webdriver
from login.login_page import LoginPage
from profile.profile_page import ProfilePage
from rate_videos.rate_videos_page import RateVideosPage
import time
from pytest import mark

# Test Setup
@mark.ui
@mark.uiratevideos
@mark.testnavigatetoratevideospage
def test_navigate_to_rate_videos_page():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    login_page.go()
    login_page.open_oAuth.click()
    time.sleep(2)
    frst_win = login_page.driver.window_handles[0]
    sec_win = login_page.driver.window_handles[1]
    login_page.driver.switch_to.window(sec_win)
    login_page.enter_email.input_text("paul.laguna@thisisnom.co")
    login_page.click_email_nxt.click()
    login_page.enter_pass.input_text("thisisnom1983")
    login_page.click_pass_nxt.click()
    login_page.driver.switch_to.window(frst_win)
    # add assertion
    rate_videos_page = RateVideosPage(driver=browser)
    rate_videos_page.rate_videos_link.click()
    # add assertion
    browser.quit()



