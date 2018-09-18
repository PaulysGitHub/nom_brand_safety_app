from selenium.webdriver.common.by import By
from .base_elem import BaseElement
from .base_page import BasePage

class LoginPage(BasePage):

    url = 'https://brandsafety.nomdata.info'

    @property
    def open_oAuth(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > '
                                    'div.login-container.d-flex.justify-content-center.align-items-center.'
                                    'animated.slideInUpTiny.animation-duration-3 > div > div > '
                                    'a.btn.btn-primary.btn-block')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def enter_email(self):
        locator = (By.CSS_SELECTOR, '#identifierId')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def click_email_nxt(self):
        locator = (By.ID, 'identifierNext')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def enter_pass(self):
        locator = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def click_pass_nxt(self):
        locator = (By.ID, "passwordNext")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def brand_unsafe_text(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > "
                                    "div:nth-child(2) > div.col-lg-6.col-md-4.col-sm-12 > "
                                    "div > div > div.jr-card-social > div > div > div > div."
                                    "row > div:nth-child(1) > p > small")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def nom_logo_link(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-container."
                                    "fixed-drawer > div > div > div > div > a > img")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def demo_account_link(self):
        locator = (By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div."
                                    "login-container.d-flex.justify-content-center.align-items-center."
                                    "animated.slideInUpTiny.animation-duration-3 > div > div > a:nth-child(2) > small")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def demo_account_password(self):
        locator = By.CSS_SELECTOR, "#demo-password"
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def demo_login_button(self):
        locator = By.CSS_SELECTOR, "#demo-login"
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def oAuth_login_link(self):
        locator = By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > " \
                                   "div > div:nth-child(2) > a:nth-child(2) > small"
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def unknown_account_error(self):
        locator = By.CSS_SELECTOR, "#demo-login-error"
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def google_auth_btn_txt(self):
        locator = By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div.login-container." \
                                   "d-flex.justify-content-center.align-items-center.animated.slideInUpTiny." \
                                   "animation-duration-3 > div > div > a.btn.btn-primary.btn-block > span"
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def password_text(self):
        locator = By.CSS_SELECTOR, "#app-site > div > div > div.app-main-content > div > div > div > div > " \
                                   "div:nth-child(1) > label"
        return BaseElement(self.driver, by=locator[0], value=locator[1])