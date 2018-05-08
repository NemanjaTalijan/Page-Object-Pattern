from Source.PageObject.Locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Home(object):

    def __init__(self, browser):

        self.browser = browser
        self.email = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, f"{Locators.email}"))
        )
        self.password = self.browser.find_element(By.NAME, f"{Locators.password}")
        self.login_button = self.browser.find_element(By.XPATH, f"{Locators.login_button}")

        self.browser_title = self.browser.title

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email.send_keys("{}".format(email))

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password.send_keys("{}".format(password))

    def get_login_button(self):
        return self.login_button

    def click_login_button(self):
        self.login_button.submit()

    def get_browser_title(self):
        return self.browser_title
