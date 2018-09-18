from selenium import webdriver
from login.login_page import LoginPage
from profile.profile_page import ProfilePage
import time
from pytest import mark

# test navigating to profile page
@mark.ui
@mark.uiprofilepage
@mark.testnavigatetoeditprofile
def test_navigate_to_edit_profile():
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
    profile_page = ProfilePage(driver=browser)
    profile_page.edit_profile_link.click()
    assert profile_page.select_an_avatar_text.text == "Select an Avatar", "Bad locator"
    browser.quit()



