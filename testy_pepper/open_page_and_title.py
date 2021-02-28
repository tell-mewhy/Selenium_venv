from test_case import TestCase
from time import sleep

class OpenPage(TestCase):

    PAGE = 'https://www.pepper.pl/'
    TITLE = 'Pepper.pl - Najlepsze Okazje, Rabaty, Promocje i Błędy Cenowe'
    DESCRIPTION = """Pepper to miejsce z najgorętszymi okazjami. Oceniaj i komentuj je z naszą społecznością ♥ Okazje, kupony, kody rabatowe, błędy cenowe na to, czego szukasz ⇒ smartfon, laptop, konsola, zabawki, moda, dom i ogród, artykuły spożywcze… ✅ Kupuj w najniższych cenach i oszczędzaj ✅ Twoja społeczność zakupowa ➤ Pepper.pl"""

    def test_page(self):
        try:
            self.driver.get(self.PAGE)
        except Exception:
            self.fail('Page not found')
        self.assertTrue(self.PAGE == self.driver.current_url)
        assert self.TITLE in self.driver.title

    def test_description(self):
        self.driver.get(self.PAGE)
        description = self.driver.find_element_by_xpath('//head//meta[@property="og:description"]')
        self.assertTrue(self._clearText(description.get_attribute('content')) == self._clearText(self.DESCRIPTION))

    def test_acceptCookies(self):
        self.driver.get(self.PAGE)
        sleep(2)
        try:
            elem = self.driver.find_element_by_xpath('//button[@class="flex--grow-1"]')
        except Exception:
            self.fail('Element not found')
        elem.click()

    def _clearText(self, text):
        return text.replace(' ','')
