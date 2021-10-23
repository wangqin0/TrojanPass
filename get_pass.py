import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options


def get_pass_and_remainder(output_image):
    # Requires Selenium WebDriver 3.13 or newer

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # if you want to use Firefox for automation then uncomment the line below:
    # with webdriver.Firefox() as driver:
    with webdriver.Chrome(chrome_options=chrome_options) as driver:
        WebDriverWait(driver, 20)

        # landing page
        driver.get("https://trojancheck.usc.edu/login")
        # driver.get
        driver.find_element_by_xpath('/html/body/app-root/app-login/main/section/div/div[1]/div[1]/button').click()

        # login page
        # wait(driver, 10)
        NETID_field = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(
                (By.ID, "username"))
        )
        NETID_field.send_keys(os.getenv('TROJAN_PASS_NETID'))
        driver.find_element_by_id('password').send_keys(os.getenv('TROJAN_PASS_PASSWORD'))
        driver.find_element_by_xpath('//*[@id="loginform"]/div[4]/button').click()

        # continue_button
        WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "/html/body/app-root/app-consent-check/main/section/section/button"))
        ).click()

        # prepare for begin_wellness_assessment
        begin_wellness_assessment = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '/html/body/app-root/app-dashboard/main/div/section[1]/div[2]/button'))
        )

        # done this before, proceed to save
        if len(driver.find_elements_by_class_name('day-pass-qr-code-box')) != 0:
            next_test_remainder = driver.find_element_by_xpath(
                '/html/body/app-root/app-dashboard/main/div/div[1]/div/div/div[2]').text
            pass_element = driver.find_element_by_xpath(
                # '/html/body/app-root/app-dashboard/main/div/section[1]')              # Pass with outer div
                # '/html/body/app-root/app-dashboard/main/div/section[1]/div')          # Pass with outer div
                # '/html/body/app-root/app-dashboard/main/div/section[1]/div/div[2]')     # Pass with outer wrapper
                '/html/body/app-root/app-dashboard/main/div/section[1]/div/div[2]/app-day-pass')      # Pass
                # '/html/body/app-root/app-dashboard/main/div/section[1]/div/div[2]/app-day-pass/div')  # Pass
            pass_element.screenshot(output_image)
            return next_test_remainder

        begin_wellness_assessment.click()

        # start_screening
        WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '/html/body/app-root/app-assessment-start/main/section[1]/div[2]/button[2]'))
        ).click()

        # select No
        for i in range(3, 6, 2):
            WebDriverWait(driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, '//*[@id="mat-button-toggle-' + str(i) + '-button"]'))
            ).click()

        WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '/html/body/app-root/app-assessment-questions/main/section/section[3]/button'))
        ).click()

        # select No
        for i in range(14, 27, 2):
            WebDriverWait(driver, 20).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, '//*[@id="mat-button-toggle-' + str(i) + '-button"]'))
            ).click()

        driver.find_element_by_xpath('/html/body/app-root/app-assessment-questions/main/section/section[8]/button').click()

        WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '//*[@id="mat-checkbox-1-input"]'))
        )

        driver.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div').click()

        driver.find_element_by_xpath('/html/body/app-root/app-assessment-review/main/section/section[11]/button').click()

        pass_element = WebDriverWait(driver, 20).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, '/html/body/app-root/app-dashboard/main/div/section[1]/div/div[2]/app-day-pass'))
        )

        next_test_remainder = driver.find_element_by_xpath(
            '/html/body/app-root/app-dashboard/main/div/div[1]/div/div/div[2]').text
        pass_element.screenshot(output_image)

        return next_test_remainder
