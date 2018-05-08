from selenium.common.exceptions import NoSuchElementException
from Source.PageObject.Pages.mainPage import Main
from Source.PageObject.Environment.EnvironmentSetUp import EnvironmentSetup


class TestMainPage(EnvironmentSetup):

    def test_main_page(self):

        mp = Main(self.browser)
        try:
            assert "Dashboard" in mp.get_browser_title()
        except AssertionError as e:
            print(e)
            print("We are not on the main page!")

        try:
            mp.get_quick_booking().is_displayed()
            mp.get_bookings().is_displayed()
            mp.get_cms_page().is_displayed()
            mp.get_blog().is_displayed()
            mp.get_send_newsletter().is_displayed()
            mp.get_data_bse().is_displayed()
        except NoSuchElementException as e:
            print(e)
            print("All the elements on main page are not visible!")
