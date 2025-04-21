from PageObjects.landing_page import LandingPage
from Utilities.custom_logger import LogGeneration
from TestCases.conftest import log_on_failure
import pytest

@pytest.mark.usefixtures("setup_class")
class Test_001_Landing_Page:

    logger = LogGeneration.loggen()



    def test_landingpageheaderpart(self,setup_class,log_on_failure):
        self.logger.info("********** Test case started: test_landingpagetitle **********")
        self.logger.info("********** Setting up the driver and navigating to the base URL **********")
        self.logger.info("********** Maximizing the window **********")
        self.logger.info("********** Waiting for the page to load **********")

        self.logger.info("********** Retrieving Landing Page title **********")
        self.landing_page_title=self.driver.title
        print("This is the landing page title:",self.landing_page_title)
        self.lp=LandingPage(self.driver)
        self.logger.info("********** Clicking Prime Page button **********")
        self.lp.click_prime_title()
        self.logger.info("********** Retrieving Prime Page title **********")
        self.prime_title=self.driver.title
        print("This is the prime page title:",self.prime_title)

        self.lp.click_yatra_prime_page_title()
        self.logger.info("********** Retrieving Landing Page title for confirmation **********")
        self.yatra_landing_page_title = self.driver.title
        expected_title = "Flight, Cheap Air Tickets , Hotels, Holiday, Trains Package Booking - Yatra.com"

        try:
            assert self.yatra_landing_page_title == expected_title, "Title did not match as expected"
            print("Title matched as expected")
        except AssertionError as e:
            print(str(e))
            raise

        self.logger.info("********** Clicking Corporates/SME Button **********")
        self.lp.click_corporate_sme_title()

        self.logger.info("********** Getting Corporates/SME dropdown results **********")
        dropdown_results = self.lp.get_corporate_sme_dropdown_results()
        self.driver.save_screenshot(".\\Screenshot\\"+"screenshot_corporate_sme_dropdown.png")

        self.logger.info("********** Printing Corporates/SME dropdown results **********")
        for result in dropdown_results:
            print(result)

        self.logger.info(f"Number of dropdown items: {len(dropdown_results)}")
        print(f"Number of dropdown items: {len(dropdown_results)}")


        parent_window_handle=self.driver.current_window_handle
        print("Parent window handle:", parent_window_handle)

        self.logger.info("********** Clicking Corporate Travel Link **********")
        self.lp.click_corporate_travel_link()


        all_window_handles=self.driver.window_handles
        print("All window handles:", all_window_handles)
        for handle in all_window_handles:
            if handle!=parent_window_handle:
                self.driver.switch_to.window(handle)
                self.logger.info("********** Switching to Corporate Travel window **********")
                print("Current window title:", self.driver.title)
                self.driver.close()
                self.driver.switch_to.window(parent_window_handle)
                self.logger.info("********** Switching back to parent window **********")

        self.logger.info("********** Clicking Corporates/SME Button **********")
        self.lp.click_corporate_sme_title()

        parent_window_handle = self.driver.current_window_handle
        print("Parent window handle:", parent_window_handle)

        self.logger.info("********** Clicking yatra M.I.C.E Link **********")
        self.lp.click_yatra_mice_link()

        all_window_handles = self.driver.window_handles
        print("All window handles:", all_window_handles)
        for handle in all_window_handles:
            if handle != parent_window_handle:
                self.driver.switch_to.window(handle)
                self.logger.info("********** Switching to yatra M.I.C.E window **********")
                print("Current window title:", self.driver.title)
                self.driver.close()
                self.driver.switch_to.window(parent_window_handle)
                self.logger.info("********** Switching back to parent window **********")


        self.logger.info("********** RECAP Link (Not working as expected so its deferred) **********")

        self.logger.info("********** Clicking For Travel Agents Button **********")
        self.driver.implicitly_wait(10)  # wait for the element to load
        self.lp.click_travel_agent_button()
        all_window_handles = self.driver.window_handles
        print("All window handles:", all_window_handles)
        for handle in all_window_handles:
            if handle != parent_window_handle:
                self.driver.switch_to.window(handle)
                self.logger.info("********** Switching to Travel Agent window **********")
                print("Current window title:", self.driver.title)
                self.driver.close()
                self.driver.switch_to.window(parent_window_handle)
                self.logger.info("********** Switching back to parent window **********")

        self.logger.info("********** Clicking Login/SignUp dropdown **********")
        self.lp.click_login_signup_button()

        self.logger.info("********** Getting Login/SignUp dropdown results **********")
        login_signup_dropdown_results = self.lp.get_login_signup_dropdown_results()
        self.driver.save_screenshot(".\\Screenshot\\"+"screenshot_login_signup_dropdown.png")


        self.logger.info("********** Printing Login/SignUp dropdown results **********")
        for login_dropdown_result in login_signup_dropdown_results:
            print(login_dropdown_result)

        self.logger.info(f"Number of dropdown items: {len(login_signup_dropdown_results)}")
        print(f"Number of dropdown items: {len(login_signup_dropdown_results)}")

        self.logger.info("********** Clicking Login/Create Account Link **********")
        self.lp.click_login_createaccount_link()
        print("Login/Create account page title:", self.driver.title)
        self.logger.info("********** Clicking yatra logo in Login/Create Account page **********")
        self.lp.click_yatra_logo_login_createaccount_page()
        self.logger.info("********** Returning back to landing page yatra.com **********")

        self.lp.click_login_signup_button()
        self.lp.click_my_booking_link()
        all_window_handles = self.driver.window_handles
        print("All window handles:", all_window_handles)
        for handle in all_window_handles:
            if handle != parent_window_handle:
                self.driver.switch_to.window(handle)
                self.logger.info("********** Switching to My Booking window **********")
                print("Current window title:", self.driver.title)
                self.driver.save_screenshot(".\\Screenshot\\" + "screenshot_My_Booking_Page.png")
                self.driver.close()
                self.driver.switch_to.window(parent_window_handle)
                self.logger.info("********** Switching back to parent window **********")

        self.lp.click_login_signup_button()
        self.lp.click_my_refund_link()
        all_window_handles = self.driver.window_handles
        print("All window handles:", all_window_handles)
        for handle in all_window_handles:
            if handle != parent_window_handle:
                self.driver.switch_to.window(handle)
                self.logger.info("********** Switching to My Refund window **********")
                print("Current window title:", self.driver.title)
                self.driver.save_screenshot(".\\Screenshot\\" + "screenshot_My_Refund_Page.png")
                self.driver.close()
                self.driver.switch_to.window(parent_window_handle)
                self.logger.info("********** Switching back to parent window **********")


    def test_flight_search(self,setup_class,log_on_failure):
        self.logger.info("********** Test case started: test_flight_search : Testing Flight Panel **********")
        self.logger.info("********** Navigating to URL **********")
        self.driver.get("https://www.yatra.com")
        self.logger.info("********** Maximizing the window **********")
        self.driver.maximize_window()

        self.logger.info("********** Retrieving Panel list buttons **********")
        multitab_results = self.lp.get_panel_multitab_title()

        message = f"Panel List items: {(multitab_results)}"
        self.logger.info(message)
        print(message)

        # Add assertions or further interactions here
        assert "Flights" in multitab_results, "Flights option not found in panel list"







































