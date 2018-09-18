from selenium.webdriver.common.by import By
from .base_elem import BaseElement
from .base_page import BasePage

class LogoutPage(BasePage):

    url = 'https://brandsafety.nomdata.info'


    @property
    def logout_link(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-container.fixed-drawer > '
                                    'div > div > div > ul > li:nth-child(5) > a')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def logout_text(self):
        locator = (By.CSS_SELECTOR, '#app-site > div > div > div.app-main-content > div > div.'
                                    'login-container.d-flex.justify-content-center.align-items-center.'
                                    'animated.slideInUpTiny.animation-duration-3 > div > div > a.'
                                    'btn.btn-primary.btn-block > span')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

