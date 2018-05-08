from Source.PageObject.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Main(object):

    def __init__(self, browser):
        self.browser = browser
        self.quick_booking = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "{}".format(Locators.quick_booking)))
        )
        self.booking = self.browser.find_element(By.CLASS_NAME, "{}".format(Locators.bookings))
        self.cms_page = self.browser.find_element(By.CLASS_NAME, "{}".format(Locators.cms_page))
        self.blog = self.browser.find_element(By.CLASS_NAME, "{}".format(Locators.blog))
        self.send_newsletter = self.browser.find_element(By.CLASS_NAME, "{}".format(Locators.send_newsletter))
        self.data_bse = self.browser.find_element(By.CLASS_NAME, "{}".format(Locators.data_bse))
        self.browser_title = self.browser.title

    def get_quick_booking(self):
        return self.quick_booking

    def get_bookings(self):
        return self.booking

    def get_cms_page(self):
        return self.cms_page

    def get_blog(self):
        return self.blog

    def click_blog(self):
        self.blog.click()

    def get_send_newsletter(self):
        return self.send_newsletter

    def get_data_bse(self):
        return self.data_bse

    def get_browser_title(self):
        return self.browser_title
