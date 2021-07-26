from selenium import webdriver
import Constants
import Locators
import time

def TestRegistration(username, email, password,password_confirmation):
    driver = webdriver.Chrome()
    driver.get(Constants.BASE_URL)
    driver.maximize_window()

    prijaviSeField=driver.find_element_by_css_selector(Locators.prijavi_se_dugme_css_selector)
    prijaviSeField.click()

    registrujteSeField=driver.find_element_by_css_selector(Locators.registrujte_se_dugme_css_selector)
    registrujteSeField.click()

    usernameField=driver.find_element_by_css_selector(Locators.registration_page_username_css_selector)
    emailField=driver.find_element_by_css_selector(Locators.registration_page_email_css_selector)
    passwordField=driver.find_element_by_css_selector(Locators.registration_page_password_css_selector)
    passwordConfirmationField=driver.find_element_by_css_selector(Locators.registration_page_password_confirmation_css_selector)

    registrationButtonField=driver.find_element_by_css_selector(Locators.registration_page_registration_button_css_selector)
    
    usernameField.send_keys(username)
    emailField.send_keys(email)
    passwordField.send_keys(password)
    passwordConfirmationField.send_keys(password)

    registrationButtonField.click()
    time.sleep(10)

TestRegistration('MasterBlaster','masterblaster008@gmail.com','MasterBlaster008','MasterBlaster008')








