import unittest

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = driver
