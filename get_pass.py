import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from utils import str_image


# Universal driver interface for Firefox or Chrome
class Driver:
    def __init__(self, firefox: bool = True, headless: bool = True):
        self.headless = headless

        if firefox:
            options = webdriver.FirefoxOptions()
            options.headless = headless
            self.driver = webdriver.Firefox(options=options)
        else:
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            self.driver = webdriver.Chrome(options=options)

    def get(self, url: str):
        self.driver.get(url)

    def name(self) -> str:
        return self.driver.name

    def ele_by_xpath(self, xpath: str) -> WebElement:
        return self.driver.find_element_by_xpath(xpath)

    def ele_by_id(self, _id: str) -> WebElement:
        return self.driver.find_element_by_id(_id)

    def ele_by_classname(self, class_name: str) -> WebElement:
        return self.driver.find_elements_by_class_name(class_name)

    def ele_with_wait(self, approach: By, locator: str, time_limit: int = 5) -> WebElement:
        return WebDriverWait(self.driver, time_limit).until(
            expected_conditions.presence_of_element_located(
                (approach, locator))
        )

    def current_url_ends(self, suffix: str) -> bool:
        return str(self.driver.current_url).endswith(suffix)


class Passer:
    def __init__(self, net_id: str, net_pw: str, driver=None, image_name: str = None, firefox: bool = True,
                 headless: bool = True):
        self.net_id = net_id
        self.net_pw = net_pw
        self.image_name = image_name or str_image(net_id)

        # recommend setting: Firefox headless or Chrome (without headless)
        self.driver = driver or Driver(firefox, headless)

    def get_pass_and_reminder(self):
        logging.info(f"Attempt to run {self.driver.name()} with headless={self.driver.headless}")

        self.login()

        if self.driver.ele_by_classname('day-pass-qr-code'):
            logging.info("Have done wellness assessment today. Saving pass")

            next_test_remainder = self.driver.ele_by_xpath(
                '/html/body/app-root/app-dashboard/main/div/div[1]/div/div/div[2]').text

            pass_element = self.driver.ele_by_xpath(
                # '/html/body/app-root/app-dashboard/main/div/section[1]/div/div[2]/app-day-pass')
                '/html/body/app-root/app-dashboard/main/div/section[1]/div/div[2]/app-day-pass/div')

            pass_element.screenshot(self.image_name)

            return next_test_remainder

        self.self_assessment()

        pass_element = self.driver.ele_with_wait(By.XPATH,
                                                 '/html/body/app-root/app-dashboard/main/div/section[1]/div/div[2]/app-day-pass')

        logging.info("Wellness assessment Completed. Saving pass")

        next_test_remainder = self.driver.ele_by_xpath(
            '/html/body/app-root/app-dashboard/main/div/div[1]/div/div/div[2]').text

        pass_element.screenshot(self.image_name)

        return next_test_remainder

    def login(self):
        self.driver.get('https://trojancheck.usc.edu/login')

        # Click the login-with-netID button
        self.driver.ele_by_xpath('/html/body/app-root/app-login/main/section/div/div[1]/div[1]/button').click()

        # Input net ID and password
        self.driver.ele_with_wait(By.ID, "username").send_keys(self.net_id)
        self.driver.ele_by_id('password').send_keys(self.net_pw)

        # Login Button
        self.driver.ele_by_xpath('//*[@id="loginform"]/div[4]/button').click()

        # Continue button
        self.driver.ele_with_wait(By.XPATH, "/html/body/app-root/app-consent-check/main/section/section/button").click()

    def self_assessment(self):
        # prepare for begin_wellness_assessment
        self.driver.ele_with_wait(By.XPATH,
                                  '/html/body/app-root/app-dashboard/main/div/section[1]/div[2]/button').click()

        # start_screening
        self.driver.ele_with_wait(By.XPATH,
                                  '/html/body/app-root/app-assessment-start/main/section[1]/div[2]/button[2]').click()

        # select No
        for i in range(3, 6, 2):
            self.driver.ele_with_wait(By.XPATH, '//*[@id="mat-button-toggle-' + str(i) + '-button"]').click()

        self.driver.ele_with_wait(By.XPATH,
                                  '/html/body/app-root/app-assessment-questions/main/section/section[3]/button').click()

        # select No
        for i in range(14, 27, 2):
            self.driver.ele_with_wait(By.XPATH, '//*[@id="mat-button-toggle-' + str(i) + '-button"]').click()

        self.driver.ele_by_xpath(
            '/html/body/app-root/app-assessment-questions/main/section/section[8]/button').click()

        # finish assessment and wait loading page
        self.driver.ele_with_wait(By.XPATH, '//*[@id="mat-checkbox-1-input"]').click()

        self.driver.ele_by_xpath('//*[@id="mat-checkbox-1"]/label/div').click()

        self.driver.ele_by_xpath(
            '/html/body/app-root/app-assessment-review/main/section/section[11]/button').click()
