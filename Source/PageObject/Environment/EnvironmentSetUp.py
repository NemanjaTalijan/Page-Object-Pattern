import unittest
from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):

    def setUp(self):

        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        # self.browser = webdriver.Chrome(chrome_options=options)
        self.browser = webdriver.Chrome()
        print("SetUp")

    def tearDown(self):
        self.browser.quit()
        print("TearDown")
