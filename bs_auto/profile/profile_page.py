from selenium.webdriver.common.by import By
from .base_elem import BaseElement
from .base_page import BasePage

class ProfilePage(BasePage):

    url = 'https://brandsafety.nomdata.info'

    @property
    def edit_profile_link(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-container.fixed-drawer > '
                                    'div > div > div > ul > li:nth-child(4) > a')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def select_an_avatar_text(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div > div > div:nth-child(1) > div:nth-child(2) > h1')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def brand_unsafe_text(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div:nth-child(2) > div.col-lg-6.col-md-4.col-sm-12 > div > div > div.jr-card-social > div > div > div > div.row > div:nth-child(1) > p > small')
        return BaseElement(self.driver, by=locator[0], value=locator[1])