import unittest
import time
from Source.PageObject.Environment.EnvironmentSetUp import EnvironmentSetup
from Source.PageObject.Pages.homePage import Home


class TestHomePage(EnvironmentSetup):

    def test_login(self):

        self.browser.get("http://www.phptravels.net/admin")

        hp = Home(self.browser)
        try:
            assert "Administator Login" in hp.get_browser_title()
        except AssertionError as e:
            print(e)
            print("We are not on the phptravels.net/admin page")

        try:
            hp.get_email().is_displayed()
            hp.get_password().is_displayed()
        except Exception as e:
            print(e)
            print("All elements not present!")

        hp.set_email("admin@phptravels.com")
        hp.set_password("demoadmin")
        hp.click_login_button()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
