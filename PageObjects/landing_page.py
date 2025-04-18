
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LandingPage:
    page_title_xpath = "//*[@id='__next']/div/div[1]/div[1]/div/div[1]/a/img"

    join_prime_title_xpath = "//img[@alt='Join Yatra Prime Banner']"
    yatra_primepage_title_xpath = "//*[@id='headerSnipe']/div/div/div[3]/div[1]/a/i"

    corporate_sme_title_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/p[1]/span[1]"
    corporate_sme_dropdown_results_xpath = "//div[@class='MuiBox-root css-iayqfd']"
    corporate_travel_link_xpath = "//body[1]/div[3]/div[3]/div[1]/div[1]/p[1]"
    yatra_mice_link_xpath = "//body[1]/div[3]/div[3]/div[1]/div[1]/p[2]"

    travel_agent_title_xpath = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/a[1]/div[1]"
    login_signup_title_xpath = "//*[@id='__next']/div/div[1]/div[1]/div/div[2]/div[3]/p"
    login_createaccount_link_xpath = "//p[normalize-space()='Login or Create Account']"
    yatra_logo_login_createaccount_page_xpath = "//a[@title='https://www.yatra.com']//i[@class='ico-newHeaderLogo']"
    my_booking_link_xpath = "//*[@id='simple-popover']/div[3]/div/div/p[2]"
    my_refund_link_xpath = "//*[@id='simple-popover']/div[3]/div/div/p[3]"

    def __init__(self, driver):
        self.driver = driver

    def click_page_title(self):
        self.driver.find_element(By.XPATH, self.page_title_xpath).click()

    def click_prime_title(self):
        self.driver.find_element(By.XPATH, self.join_prime_title_xpath).click()

    def click_yatra_prime_page_title(self):
        self.driver.find_element(By.XPATH, self.yatra_primepage_title_xpath).click()

    def click_corporate_sme_title(self):
        self.driver.find_element(By.XPATH, self.corporate_sme_title_xpath).click()

    def get_corporate_sme_dropdown_results(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='MuiBox-root css-iayqfd']"))
            )
            dropdown_results = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-iayqfd']")
            return [result.text for result in dropdown_results]
        except Exception as e:
            print(f"Error getting dropdown results: {str(e)}")
            return []

    def click_corporate_travel_link(self):
        corporate_travel_link_xpath = (WebDriverWait(self.driver,10).until
                                       (EC.element_to_be_clickable(
            (By.XPATH,"//body[1]/div[3]/div[3]/div[1]/div[1]/p[1]"))))
        corporate_travel_link_xpath.click()
        #self.driver.find_element(By.XPATH, self.corporate_travel_link_xpath).click()

    def click_yatra_mice_link(self):
        self.driver.find_element(By.XPATH, self.yatra_mice_link_xpath).click()

    def click_travel_agent_button(self):
        travel_agent_title_xpath = (WebDriverWait(self.driver, 30).until
            (EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='__next']/div/div[1]/div[1]/div/div[2]/div[2]/a"))))
        travel_agent_title_xpath.click()
        #self.driver.find_element(By.XPATH, self.travel_agent_title_xpath).click()

    def click_login_signup_button(self):
        self.driver.find_element(By.XPATH, self.login_signup_title_xpath).click()

    def get_login_signup_dropdown_results(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='MuiBox-root css-iayqfd']"))
            )
            dropdown_results = self.driver.find_elements(By.XPATH, "//div[@class='MuiBox-root css-iayqfd']")
            return [result.text for result in dropdown_results]
        except Exception as e:
            print(f"Error getting dropdown results: {str(e)}")
            return []

    def click_login_createaccount_link(self):
        self.driver.find_element(By.XPATH, self.login_createaccount_link_xpath).click()

    def click_yatra_logo_login_createaccount_page(self):
        self.driver.find_element(By.XPATH, self.yatra_logo_login_createaccount_page_xpath).click()

    def click_my_booking_link(self):
        self.driver.find_element(By.XPATH, self.my_booking_link_xpath).click()

    def click_my_refund_link(self):
        self.driver.find_element(By.XPATH, self.my_refund_link_xpath).click()









