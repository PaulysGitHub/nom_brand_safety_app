from selenium.webdriver.common.by import By
from .base_elem import BaseElement
from .base_page import BasePage

class RateVideosPage(BasePage):

    url = 'https://brandsafety.nomdata.info'


    @property
    def rate_videos_link(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-container.fixed-drawer > div > '
                                    'div > div > ul > li:nth-child(5) > a')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def rate_videos_text(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > '
                                    'div:nth-child(2) > div.col-lg-6.col-md-4.col-sm-12 > div > '
                                    'div > div.jr-card-social > div > div > div > div.row > div:nth-child(3) > '
                                    'p > small')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

