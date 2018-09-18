from selenium import webdriver
from login.login_page import LoginPage
from profile.profile_page import ProfilePage
from rate_videos.rate_videos_page import RateVideosPage
from logout.logout_page import LogoutPage
from leaderboard.leaderboard_page import LeaderboardPage
from interest.interest_page import InterestPage
import time
from pytest import mark

# test logout from Rate Videos page
@mark.ui
@mark.uilogout
@mark.testlogoutelementsfromratevideospage
def test_logout_elements_from_rate_videos():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    login_page.go()
    login_page.nom_logo_link.find()
    login_page.open_oAuth.find()
    login_page.google_auth_btn_txt.find()
    assert login_page.google_auth_btn_txt.text == 'Google Auth', 'Cannot find element'
    login_page.demo_account_link.find()
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
    login_page.nom_logo_link.find()
    # assert login_page.dashboard_link.text == 'Brand Unsafe', 'Incorrect text'
    logout_page = LogoutPage(driver=browser)
    logout_page.logout_link.find()
    assert logout_page.logout_link.text == 'Logout', 'Not correct text'
    logout_page.logout_link.click()
    assert logout_page.logout_text.text == 'Google Auth', 'Unexpected text'
    browser.quit()

# test logout from Leaderboard page
@mark.ui
@mark.uilogout
@mark.testlogoutfromleaderboard
def test_logout_from_leaderboard():
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
    # assert login_page.dashboard_link.text == 'Brand Unsafe', 'Incorrect text'
    logout_page = LogoutPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    leaderboard_page.leaderboard_link.click()
    assert leaderboard_page.leaderboard_last_7_days_text.text == 'Leaderboard - Last 7 Days', 'Unexpeceted text not found'
    logout_page.logout_link.click()
    assert logout_page.logout_text.text == 'Google Auth', 'Unexpected text'
    browser.quit()

# test logout from Edit Interest page
@mark.ui
@mark.uilogout
@mark.testlogoutfromeditinterests
def test_logout_from_edit_interest():
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
    # assert login_page.dashboard_link.text == 'Brand Unsafe', 'Incorrect text'
    logout_page = LogoutPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
    leaderboard_page.leaderboard_link.click()
    assert leaderboard_page.leaderboard_last_7_days_text.text == 'Leaderboard - Last 7 Days', 'Unexpeceted text not found'
    logout_page.logout_link.click()
    browser.quit()

# test logout from edit profile page
@mark.ui
@mark.uilogout
@mark.testlogoutfromeditprofile
def test_logout_from_edit_profile():
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
    # assert login_page.dashboard_link.text == 'Brand Unsafe', 'Incorrect text'
    logout_page = LogoutPage(driver=browser)
    profile_page = ProfilePage(driver=browser)
    profile_page.edit_profile_link.click()
    logout_page.logout_link.click()
    browser.quit()
