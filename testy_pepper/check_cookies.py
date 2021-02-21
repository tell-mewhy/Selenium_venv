# https://chercher.tech/python/python-selenium-cookies

from test_case import TestCase

from selenium.webdriver.support.ui import WebDriverWait

class CheckCookies(TestCase):

    PAGE = 'https://www.pepper.pl/'

    def test_cookies(self):

        try:
            self.driver.get(self.PAGE)
        except Exception:
            self.fail('Not found')
        self.assertTrue((self.driver.get_cookies()))

        
        # print(self.driver.get_cookies())

        # self.driver.delete_all_cookies()
