from selenium.webdriver.common.by import By
from .base_elem import BaseElement
from .base_page import BasePage

class LeaderboardPage(BasePage):

    url = 'https://brandsafety.nomdata.com'


    @property
    def leaderboard_link(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-container.fixed-drawer > div > div > '
                                    'div > ul > li:nth-child(1) > a')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def leaderboard_last_7_days_text(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(2) > '
                                    'div:nth-child(1) > div.jr-entry-header > h3 > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def two_days_icon(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(1) > div > div > div > div.col-sm-3 > div > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def two_day_amount(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(1) > div > div > div > div.col-sm-9 > h4 > strong')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def two_day_rating_txt(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(1) > div > div > div > div.col-sm-9 > h4 > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def svn_days_icon(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(2) > div > div > div > div.col-sm-3 > div > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def svn_day_amount(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(2) > div > div > div > div.col-sm-9 > h4 > strong')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def svn_day_rating_txt(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(2) > div > div > div > div.col-sm-9 > h4 > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def thirty_days_icon(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(3) > div > div > div > div.col-sm-3 > div > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def thirty_day_amount(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(3) > div > div > div > div.col-sm-9 > h4 > strong')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def thirty_day_rating_txt(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(3) > div > div > div > div.col-sm-9 > h4 > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def all_time_icon(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(4) > div > div > div > div.col-sm-3 > div > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def all_time_amount(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                    'div > div:nth-child(4) > div > div > div > div.col-sm-9 > h4 > strong')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def all_time_rating_txt(self):
        locator  = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(1) > div > '
                                     'div > div:nth-child(4) > div > div > div > div.col-sm-9 > h4 > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])


    @property
    def avatar_img(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(2) > '
                                    'div:nth-child(1) > div.p-0.overflow-hidden.border-0 > div > div > '
                                    'div:nth-child(1) > div > li > div > div.mr-3.mb-2 > span > img')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def profile_name(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(2) '
                                    '> div:nth-child(1) > div.p-0.overflow-hidden.border-0 > div > div > '
                                    'div:nth-child(1) > div > li > div > div.media-body > h3')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def user_rating_last_7_days(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(2) '
                                    '> div:nth-child(1) > div.p-0.overflow-hidden.border-0 > div > div > '
                                    'div:nth-child(1) > div > li > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def activities_header(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(2) > '
                                    'div:nth-child(2) > div.jr-entry-header > h3 > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])


