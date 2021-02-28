from test_case import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class CheckNowe(TestCase):
    """Test"""

    PAGE = 'https://www.pepper.pl/'

    def test_checksearch(self):
        try:
            self.driver.get(self.PAGE)
            klik = self.driver.find_element_by_link_text('Nowe')
            sleep(3)
            klik.click()
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, 'Elektronika'))
            )
            element.click()
            self.driver.back()
            
            sleep(3)
        except Exception:
            self.fail('Element Nowe e.g. 3 not found')
