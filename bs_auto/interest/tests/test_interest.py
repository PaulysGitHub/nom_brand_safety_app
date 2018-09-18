from selenium import webdriver
from login.login_page import LoginPage
from profile.profile_page import ProfilePage
from leaderboard.leaderboard_page import LeaderboardPage
from interest.interest_page import InterestPage
import time
from pytest import mark


# Login via oAuth and navigate to edit interest page
@mark.ui
@mark.uiinterest
@mark.testnavigatetointerestpage
def test_navigate_to_interest_page():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
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
    interest_page.edit_interest_link.find()
    assert interest_page.edit_interest_link.text == "Edit Interests", "Can't find element or wrong text."
    interest_page.edit_interest_link.click()
    interest_page.interests_header_text.find()
    assert interest_page.interests_header_text.text == "Interests", "Can't find element or wrong text."
    browser.quit()

# Test Edit Interest search box
@mark.ui
@mark.uiinterest
@mark.testinterestsearchbox
def test_interest_search_box():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
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
    interest_page.edit_interest_link.find()
    assert interest_page.edit_interest_link.text == "Edit Interests", "Can't find element or wrong text."
    interest_page.edit_interest_link.click()
    interest_page.interests_header_text.find()
    assert interest_page.interests_header_text.text == "Interests", "Can't find element or wrong text."

    interest_page.interest_search_box.find()
    interest_page.interest_search_box.input_text("science")
    assert interest_page.interest_catagory_science.text == "Arts & Entertainment > Movies > Science Fiction & " \
                                                           "Fantasy Films", \
                                                            "Can't find element or wrong text."
    browser.quit()

# Test Edit Interest search box then click btn
@mark.ui
@mark.uiinterest
@mark.testinterestsearchboxthenedit
def test_interest_search_box_then_edit():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
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
    interest_page.edit_interest_link.find()
    assert interest_page.edit_interest_link.text == "Edit Interests", "Can't find element or wrong text."
    interest_page.edit_interest_link.click()
    interest_page.interests_header_text.find()
    assert interest_page.interests_header_text.text == "Interests", "Can't find element or wrong text."

    interest_page.interest_search_box.find()
    interest_page.interest_search_box.input_text("science")
    assert interest_page.interest_catagory_science.text == "Arts & Entertainment > Movies > Science Fiction & " \
                                                           "Fantasy Films", \
                                                            "Can't find element or wrong text."
    interest_page.edit_interest_button_link.find()
    assert interest_page.edit_interest_button_link.text == "Edit Interest", "Can't find text."
    interest_page.edit_interest_button_link.click()

    # interest stats
    interest_page.suggest_tags_button_link.find()
    assert interest_page.suggest_tags_button_link.text == "Suggest Tags", "Can't find text."
    browser.quit()

# Test page pagination
@mark.ui
@mark.uiinterest
@mark.testinterestpagination
def test_interest_pagination ():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
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
    interest_page.edit_interest_link.find()
    assert interest_page.edit_interest_link.text == "Edit Interests", "Can't find element or wrong text."
    interest_page.edit_interest_link.click()
    interest_page.interests_header_text.find()
    assert interest_page.interests_header_text.text == "Interests", "Can't find element or wrong text."

    # Need more assertions here
    interest_page.next_button.find()
    interest_page.next_button.click()
    time.sleep(2)

    interest_page.previous_button.find()
    interest_page.previous_button.click()
    time.sleep(2)

    interest_page.second_page_button.find()
    interest_page.second_page_button.click()
    time.sleep(2)

    interest_page.first_page_button.find()
    interest_page.first_page_button.click()
    time.sleep(2)
    browser.quit()

# test Edit Interest dropdown; 10, 25, 50, 100
@mark.ui
@mark.uiinterest
@mark.testinterestdropdown
def test_interest_dropdown():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
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
    interest_page.edit_interest_link.find()
    assert interest_page.edit_interest_link.text == "Edit Interests", "Can't find element or wrong text."
    interest_page.edit_interest_link.click()
    interest_page.interests_header_text.find()
    assert interest_page.interests_header_text.text == "Interests", "Can't find element or wrong text."

    #add entries viewed from dropdown
    interest_page.create_interest_dropdown.find()
    interest_page.interest_show_entries_choose_10.find()
    interest_page.interest_show_entries_choose_10.click()
    # assert interest_page.interest_show_entries_amount_results.text == "Showing 1 to 10 of 1,086 entries", "Error." #prod
    assert interest_page.interest_show_entries_amount_results.text == "Showing 1 to 10 of 1,096 entries", "Error." #stage

    interest_page.interest_show_entries_choose_25.find()
    interest_page.interest_show_entries_choose_25.click()
    # assert interest_page.interest_show_entries_amount_results.text == "Showing 1 to 25 of 1,086 entries", "Error." #prod
    assert interest_page.interest_show_entries_amount_results.text == "Showing 1 to 25 of 1,096 entries", "Error." #stage

    interest_page.interest_show_entries_choose_50.find()
    interest_page.interest_show_entries_choose_50.click()
    # assert interest_page.interest_show_entries_100_results.text == "Showing 1 to 50 of 1,086 entries", "Error." #prod
    assert interest_page.interest_show_entries_amount_results.text == "Showing 1 to 50 of 1,096 entries", "Error." #stage

    interest_page.interest_show_entries_choose_100.find()
    interest_page.interest_show_entries_choose_100.click()
    interest_page.interest_show_entries_amount_results.find()
    # assert interest_page.interest_show_entries_amount_results.text == "Showing 1 to 100 of 1,086 entries", "Error." #prod
    assert interest_page.interest_show_entries_amount_results.text == "Showing 1 to 100 of 1,096 entries", "Error." #stage

    browser.quit()

# test identifying all elements of Edit Interest page
@mark.ui
@mark.uiinterest
@mark.interestsidentifyallelements
def test_all_interests_elements():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
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
    interest_page.edit_interest_link.find()
    assert interest_page.edit_interest_link.text == "Edit Interests", "Can't find element or wrong text."
    interest_page.edit_interest_link.click()
    interest_page.interests_header_text.find()
    assert interest_page.interests_header_text.text == "Interests", "Can't find element or wrong text."
    interest_page.nom_logo.find()
    interest_page.leaderboard_lnk_from_interest.find()
    assert interest_page.leaderboard_lnk_from_interest.text == "Leaderboard", "Can't find element or wrong text."
    interest_page.rate_videos_lnk_from_interest.find()
    assert interest_page.rate_videos_lnk_from_interest.text == "Rate Videos", "Can't find element or wrong text."
    interest_page.edit_interests_from_interest.find()
    assert interest_page.edit_interests_from_interest.text == "Edit Interests", "Can't find element or wrong text"
    interest_page.edit_profile_from_interest.find()
    assert interest_page.edit_profile_from_interest.text == "Edit Profile", "Can't find element or wrong text."
    interest_page.logout_from_interest.find()
    assert interest_page.logout_from_interest.text == "Logout", "Can't find element or wrong text."
    interest_page.create_new_interest_btn.find()
    assert interest_page.create_new_interest_btn.text == "Create New Interest", "Can't find element or wrong text."
    interest_page.create_interest_dropdown.find()
    interest_page.interest_search_box.find()
    interest_page.interest_datatable_header.find()
    assert interest_page.interest_datatable_header.text == "Interest", "Can't find element or wrong text."
    interest_page.interest_datatable_sort.find()
    interest_page.edit_interest_button_link.find()
    assert interest_page.edit_interest_button_link.text == "Edit Interest", "Can't find element or wrong text."
    interest_page.showing_entries.find()
    interest_page.previous_button.find()
    assert interest_page.previous_button.text == "Previous", "Can't find element or wrong text."
    interest_page.next_button.find()
    assert interest_page.next_button.text == "Next", "Can't find element or wrong text."
    interest_page.second_page_button.find()
    assert interest_page.second_page_button.text == "2", "Can't find element or wrong text."
    interest_page.first_page_button.find()
    assert interest_page.first_page_button.text == "1", "Cant' find element or wrong text."
    browser.quit()

# test identifying all elements of interest stats page
@mark.ui
@mark.uiinterest
@mark.interestsidentifyallelementsstats
def test_all_interests_elements_stats():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
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
    interest_page.edit_interest_link.find()
    assert interest_page.edit_interest_link.text == "Edit Interests", "Can't find element or wrong text."
    interest_page.edit_interest_link.click()
    interest_page.interests_header_text.find()
    assert interest_page.interests_header_text.text == "Interests", "Can't find element or wrong text."
    interest_page.nom_logo.find()
    interest_page.leaderboard_lnk_from_interest.find()
    assert interest_page.leaderboard_lnk_from_interest.text == "Leaderboard", "Can't find element or wrong text."
    interest_page.rate_videos_lnk_from_interest.find()
    assert interest_page.rate_videos_lnk_from_interest.text == "Rate Videos", "Can't find element or wrong text."
    interest_page.edit_interests_from_interest.find()
    assert interest_page.edit_interests_from_interest.text == "Edit Interests", "Can't find element or wrong text"
    interest_page.edit_profile_from_interest.find()
    assert interest_page.edit_profile_from_interest.text == "Edit Profile", "Can't find element or wrong text."
    interest_page.logout_from_interest.find()
    assert interest_page.logout_from_interest.text == "Logout", "Can't find element or wrong text."
    interest_page.create_new_interest_btn.find()
    assert interest_page.create_new_interest_btn.text == "Create New Interest", "Can't find element or wrong text."
    interest_page.create_interest_dropdown.find()
    interest_page.interest_search_box.find()
    interest_page.interest_datatable_header.find()
    assert interest_page.interest_datatable_header.text == "Interest", "Can't find element or wrong text."
    interest_page.interest_datatable_sort.find()
    interest_page.edit_interest_button_link.find()
    assert interest_page.edit_interest_button_link.text == "Edit Interest", "Can't find element or wrong text."
    interest_page.showing_entries.find()
    interest_page.previous_button.find()
    assert interest_page.previous_button.text == "Previous", "Can't find element or wrong text."
    interest_page.next_button.find()
    assert interest_page.next_button.text == "Next", "Can't find element or wrong text."
    interest_page.second_page_button.find()
    assert interest_page.second_page_button.text == "2", "Can't find element or wrong text."
    interest_page.first_page_button.find()
    assert interest_page.first_page_button.text == "1", "Cant' find element or wrong text."

    # interest page stats
    interest_page.edit_interest_button_link.click()
    interest_page.suggest_tags_button_link.find()
    interest_page.interest_title.find()
    interest_page.datatable_tag_name_header.find()
    assert interest_page.datatable_tag_name_header.text == "Tag Name", "Can't find element or wrong text."
    interest_page.datatable_system_tag_header.find()
    assert interest_page.datatable_system_tag_header.text == "System Tag", "Can't find element or wrong text."
    interest_page.nom_logo.find()
    interest_page.leaderboard_lnk_from_interest.find()
    assert interest_page.leaderboard_lnk_from_interest.text == "Leaderboard", "Can't find element or wrong text."
    interest_page.rate_videos_lnk_from_interest.find()
    assert interest_page.rate_videos_lnk_from_interest.text == "Rate Videos", "Can't find element or wrong text."
    interest_page.edit_interests_from_interest.find()
    assert interest_page.edit_interests_from_interest.text == "Edit Interests", "Can't find element or wrong text"
    interest_page.edit_profile_from_interest.find()
    assert interest_page.edit_profile_from_interest.text == "Edit Profile", "Can't find element or wrong text."
    interest_page.logout_from_interest.find()
    assert interest_page.logout_from_interest.text == "Logout", "Can't find element or wrong text."
    browser.quit()

# test all elements of Suggested Tags page
@mark.ui
@mark.uiinterest
@mark.interestsidentifyallelementssuggesttags
def test_all_interests_elements_sugg_tags():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    leaderboard_page = LeaderboardPage(driver=browser)
    interest_page = InterestPage(driver=browser)
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
    interest_page.edit_interest_link.find()
    assert interest_page.edit_interest_link.text == "Edit Interests", "Can't find element or wrong text."
    interest_page.edit_interest_link.click()
    interest_page.interests_header_text.find()
    assert interest_page.interests_header_text.text == "Interests", "Can't find element or wrong text."
    interest_page.nom_logo.find()
    interest_page.leaderboard_lnk_from_interest.find()
    assert interest_page.leaderboard_lnk_from_interest.text == "Leaderboard", "Can't find element or wrong text."
    interest_page.rate_videos_lnk_from_interest.find()
    assert interest_page.rate_videos_lnk_from_interest.text == "Rate Videos", "Can't find element or wrong text."
    interest_page.edit_interests_from_interest.find()
    assert interest_page.edit_interests_from_interest.text == "Edit Interests", "Can't find element or wrong text"
    interest_page.edit_profile_from_interest.find()
    assert interest_page.edit_profile_from_interest.text == "Edit Profile", "Can't find element or wrong text."
    interest_page.logout_from_interest.find()
    assert interest_page.logout_from_interest.text == "Logout", "Can't find element or wrong text."
    interest_page.create_new_interest_btn.find()
    assert interest_page.create_new_interest_btn.text == "Create New Interest", "Can't find element or wrong text."
    interest_page.create_interest_dropdown.find()
    interest_page.interest_search_box.find()
    interest_page.interest_datatable_header.find()
    assert interest_page.interest_datatable_header.text == "Interest", "Can't find element or wrong text."
    interest_page.interest_datatable_sort.find()
    interest_page.edit_interest_button_link.find()
    assert interest_page.edit_interest_button_link.text == "Edit Interest", "Can't find element or wrong text."
    interest_page.showing_entries.find()
    interest_page.previous_button.find()
    assert interest_page.previous_button.text == "Previous", "Can't find element or wrong text."
    interest_page.next_button.find()
    assert interest_page.next_button.text == "Next", "Can't find element or wrong text."
    interest_page.second_page_button.find()
    assert interest_page.second_page_button.text == "2", "Can't find element or wrong text."
    interest_page.first_page_button.find()
    assert interest_page.first_page_button.text == "1", "Cant' find element or wrong text."

    # interest page stats
    interest_page.edit_interest_button_link.click()
    interest_page.suggest_tags_button_link.find()
    interest_page.interest_title.find()
    interest_page.datatable_tag_name_header.find()
    assert interest_page.datatable_tag_name_header.text == "Tag Name", "Can't find element or wrong text."
    interest_page.datatable_system_tag_header.find()
    assert interest_page.datatable_system_tag_header.text == "System Tag", "Can't find element or wrong text."
    interest_page.nom_logo.find()
    interest_page.leaderboard_lnk_from_interest.find()
    assert interest_page.leaderboard_lnk_from_interest.text == "Leaderboard", "Can't find element or wrong text."
    interest_page.rate_videos_lnk_from_interest.find()
    assert interest_page.rate_videos_lnk_from_interest.text == "Rate Videos", "Can't find element or wrong text."
    interest_page.edit_interests_from_interest.find()
    assert interest_page.edit_interests_from_interest.text == "Edit Interests", "Can't find element or wrong text"
    interest_page.edit_profile_from_interest.find()
    assert interest_page.edit_profile_from_interest.text == "Edit Profile", "Can't find element or wrong text."
    interest_page.logout_from_interest.find()
    assert interest_page.logout_from_interest.text == "Logout", "Can't find element or wrong text."

    #  suggest tags page
    interest_page.suggest_tags_button_link.click()
    interest_page.interest_title_header.find()
    interest_page.interest_text_instructions.find()
    interest_page.go_back_button.find()
    interest_page.interest_current_tags.find()
    interest_page.tags_research_title.find()
    interest_page.tags_research_text_instructions.find()
    interest_page.tags_research_text_box.find()
    interest_page.tags_research_clear_list_btn.find()
    interest_page.tags_suggest_tags_btn.find()
    interest_page.suggested_tags_header.find()
    interest_page.suggested_dropdown.find()
    interest_page.suggested_tags_search_box.find()
    interest_page.suggested_tags_tag_name_datatable_header.find()
    interest_page.suggested_tags_system_tag_datatable_header.find()
    interest_page.suggested_tags_score_datatable_header.find()
    interest_page.suggested_tags_matched_datatable_header.find()
    interest_page.suggested_tags_top_matches_datatable_header.find()
    interest_page.suggested_tags_show_entries_results.find()
    interest_page.suggested_tags_previous_btn.find()
    interest_page.suggested_tags_next_btn.find()

    interest_page.nom_logo.find()
    interest_page.leaderboard_lnk_from_interest.find()
    assert interest_page.leaderboard_lnk_from_interest.text == "Leaderboard", "Can't find element or wrong text."
    interest_page.rate_videos_lnk_from_interest.find()
    assert interest_page.rate_videos_lnk_from_interest.text == "Rate Videos", "Can't find element or wrong text."
    interest_page.edit_interests_from_interest.find()
    assert interest_page.edit_interests_from_interest.text == "Edit Interests", "Can't find element or wrong text"
    interest_page.edit_profile_from_interest.find()
    assert interest_page.edit_profile_from_interest.text == "Edit Profile", "Can't find element or wrong text."
    interest_page.logout_from_interest.find()
    assert interest_page.logout_from_interest.text == "Logout", "Can't find element or wrong text."
    browser.quit()
