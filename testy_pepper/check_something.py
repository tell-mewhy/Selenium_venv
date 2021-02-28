from test_case import TestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Something(TestCase):

    PAGE = 'https://www.pepper.pl/'

    def test_something(self):

        try:
            self.driver.get(self.PAGE)

            # wait = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
            #   "//div[@class='popover-cover zIndex--fixed fade v-leave-to']")))

            elem = self.driver.find_element_by_xpath('//button[@class="flex--grow-1"]')
            sleep(2)
            elem.click()
            sleep(2)

            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT,'Komentowane'))
            )
            element.click()

        except Exception:
            self.fail('Page not found')

        sleep(5)
