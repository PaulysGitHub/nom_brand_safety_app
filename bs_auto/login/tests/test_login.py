from selenium import webdriver
from login.login_page import LoginPage
import time
from pytest import mark

# Test for all elements of login page
@mark.ui
@mark.uilogin
@mark.testallelementslogin
def test_all_elements_login():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    login_page.go()
    # login
    login_page.nom_logo_link.find()
    login_page.open_oAuth.find()
    login_page.google_auth_btn_txt.find()
    assert login_page.google_auth_btn_txt.text == 'Google Auth', 'Cannot find element'
    login_page.demo_account_link.find()
    assert login_page.demo_account_link.text == 'Demo Account?', 'Cannot find element'
    login_page.demo_account_link.click()
    # demo account?
    login_page.password_text.find()
    assert login_page.password_text.text == 'Password', 'Cannot find element'
    login_page.demo_account_password.find()
    login_page.demo_login_button.find()
    assert login_page.demo_login_button.text == 'Demo Login', 'Cannot find element'
    login_page.oAuth_login_link.find()
    assert login_page.oAuth_login_link.text == 'OAuth Login?', 'Cannot find element'
    browser.quit()

# test login successful
@mark.ui
@mark.uilogin
@mark.testloginsuccess
def test_login_success():
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
    assert login_page.brand_unsafe_text.text == 'Brand Unsafe', 'Unexpected dashboard link text'
    browser.quit()

# test demo account link
@mark.ui
@mark.uilogin
@mark.testdemoaccountlink
def test_demo_account_link():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    login_page.go()
    login_page.demo_account_link.click()
    assert login_page.oAuth_login_link.text == "OAuth Login?", "Wrong text"
    browser.quit()

# test demo account link wrong password
@mark.ui
@mark.uilogin
@mark.testdemoaccountlinkwrongpassword
def test_demo_account_link_wrong_password():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    login_page.go()
    login_page.demo_account_link.click()
    assert login_page.oAuth_login_link.text == "OAuth Login?", "Wrong text"
    browser.quit()

# test demo account wrong password
@mark.ui
@mark.uilogin
@mark.testdemoaccountwrongpassword
def test_demo_account_wrong_password():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    login_page.go()
    login_page.demo_account_link.click()
    assert login_page.oAuth_login_link.text == "OAuth Login?", "Wrong text"
    login_page.demo_account_password.input_text("test fail")
    login_page.demo_login_button.click()
    assert login_page.unknown_account_error.text == "Unknown account", "Text not found"
    browser.quit()

# test demo account oAuth return link
@mark.ui
@mark.uilogin
@mark.testdemoaccountoauthreturnlink
def test_demo_account_oauth_return_link():
    browser = webdriver.Chrome()
    login_page = LoginPage(driver=browser)
    login_page.go()
    login_page.demo_account_link.click()
    assert login_page.oAuth_login_link.text == "OAuth Login?", "Wrong text"
    login_page.demo_account_password.input_text("test fail")
    login_page.demo_login_button.click()
    assert login_page.unknown_account_error.text == "Unknown account", "Text not found"
    login_page.oAuth_login_link.click()
    assert login_page.demo_account_link.text == "Demo Account?", "Wrong text"
    browser.quit()

     # Need to write test for successful test account login
     # Need to write test for checking all elements
     # Need to add more assertions
     # Need to write more tests for Edit Interests
