from selenium import webdriver
from login.login_page import LoginPage
from profile.profile_page import ProfilePage
from leaderboard.leaderboard_page import LeaderboardPage
import time
from pytest import mark

# test navigate to leaderboard page
@mark.ui
@mark.uileaderboard
@mark.testnavigatetoleaderboard
def test_navigate_to_leaderboard_page():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
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
    leaderboard_page.leaderboard_link.click()
    assert leaderboard_page.leaderboard_last_7_days_text.text == 'Leaderboard - Last 7 Days', 'Incorrect text'
    leaderboard_page.two_days_icon.find()
    assert leaderboard_page.two_days_icon.text == '2 DAYS', 'Incorrect element text'
    leaderboard_page.two_day_amount.find()
    leaderboard_page.two_day_rating_txt.find()
    assert leaderboard_page.two_day_rating_txt.text == 'Ratings', 'Incorrect element text'

    leaderboard_page.svn_days_icon.find()
    assert leaderboard_page.svn_days_icon.text == '7 DAYS', 'Incorrect element text'
    leaderboard_page.svn_day_amount.find()
    leaderboard_page.svn_day_rating_txt.find()
    assert leaderboard_page.svn_day_rating_txt.text == 'Ratings', 'Incorrect element text'

    leaderboard_page.thirty_days_icon.find()
    assert leaderboard_page.thirty_days_icon.text == '30 DAYS', 'Incorrect element text'
    leaderboard_page.thirty_day_amount.find()
    leaderboard_page.thirty_day_rating_txt.find()
    assert leaderboard_page.thirty_day_rating_txt.text == 'Ratings', 'Incorrect element text'

    leaderboard_page.all_time_icon.find()
    assert leaderboard_page.all_time_icon.text == 'ALL-TIME', 'Incorrect element text'
    leaderboard_page.all_time_amount.find()
    leaderboard_page.all_time_rating_txt.find()
    assert leaderboard_page.all_time_rating_txt.text == 'Ratings', 'Incorrect element text'

    leaderboard_page.avatar_img.find()
    leaderboard_page.profile_name.find()
    leaderboard_page.user_rating_last_7_days.find()
    leaderboard_page.activities_header.find()
    assert leaderboard_page.activities_header.text == 'Activities', 'Incorrect element text'


    # Navigate to Edit Interests

    # Navigate to Video Rating

    # Navigate to Profile page

    # Logout

    browser.quit()



