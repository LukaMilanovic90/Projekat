from selenium import webdriver 
import time
import Constants
import Locators


def LogoutPageTest(email,password):
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

    time.sleep(10)

    logoutButton=driver.find_element_by_css_selector(Locators.logout_page_logout_button_css_selector)
    logoutButton.click()
    time.sleep(3)

    if(driver.current_url==Constants.BASE_URL):
        print('Uspesno izlogovan')

    time.sleep(20)

LogoutPageTest('masterblaster008@gmail.com','MasterBlaster008')