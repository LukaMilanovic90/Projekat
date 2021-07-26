from selenium import webdriver
import time
import Constants
import Locators
import MockedData


def TestLogin(email, password):
    driver=webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    prijaviSe=driver.find_element_by_css_selector(Locators.prijavi_se_dugme_css_selector)
    prijaviSe.click()

    emailField = driver.find_element_by_css_selector(Locators.login_page_email_button_css_selector)
    passwordField = driver.find_element_by_css_selector(Locators.login_page_password_button_css_selector)

    loginButtonField = driver.find_element_by_css_selector(Locators.login_page_login_button_css_selector)

    emailField.send_keys(email)
    passwordField.send_keys(password)

    loginButtonField.click()
    time.sleep(3)

test_data=MockedData.getTestData()
for podatak in test_data:
    TestLogin(podatak["email"],podatak["password"])