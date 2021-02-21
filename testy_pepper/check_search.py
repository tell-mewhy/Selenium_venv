from test_case import TestCase
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckSearch(TestCase):

    PAGE = 'https://www.pepper.pl/'

    def test_checksearch(self):
        self.driver.get(self.PAGE)
        try:
            elem = self.driver.find_element_by_xpath('//input[@name="q"]')
            elem.click()
        except Exception:
            self.fail('Element not found')

    def test_write_search(self):
        self.driver.get(self.PAGE)

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@name="q"]'))
            )
        except Exception:
            self.fail('Element not found')

        szukaj = 'test'
        element.send_keys(szukaj)
        element.submit()#click()
        sleep(3)
        self.driver.get_screenshot_as_file('foo.png')
        sleep(3)
