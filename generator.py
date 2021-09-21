import os
import yaml

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

path = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(path, 'accounts', 'accounts.txt')

with open(path) as file:
    for line in file:
        print(line.split())


def load_config():
    print("Loading config")
    with open("config.yml", "r") as f:
        global config
        config = yaml.safe_load(f)
    print("Loaded config!")


class CheckRegister(object):
    def __call__(self, driver):
        try:
            emailOrPhone = driver.find_element_by_name('emailOrPhone')
            emailOrPhone.send_keys('test@test.com')
            fullName = driver.find_element_by_name('fullName')
            fullName.send_keys('Test Test')
            username = driver.find_element_by_name('username')
            username.send_keys('test')
            password = driver.find_element_by_name('password')
            password.send_keys('test')
            return ""
        except StaleElementReferenceException:
            return False

def main():
    load_config()
    driver = webdriver.Chrome(config.get("driver_file_path", "chromedriver.exe"))
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    try:
        WebDriverWait(driver, timeout=180, poll_frequency=1).until(CheckRegister())
    except TimeoutException:
        print("Operation took too long")
    print("Done!")
    
if __name__ == "__main__":
    main()
