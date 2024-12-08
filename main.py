from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

class WebAutomation:
    def __init__(self):
        # Define driver, options and service
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        service = Service('chromedriver-win64/chromedriver.exe')
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Load the webpage
        self.driver.get('https://demoqa.com/login')

        # Locate username, password and login button
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = self.driver.find_element(By.ID, 'login')

        # Fill in username, password and click button
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Locate the elements dropdown and text box
        elements = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')
        self.driver.execute_script("arguments[0].click();", elements)

        text_box = self.driver.find_element(By.ID, 'item-0')
        self.driver.execute_script("arguments[0].click();", text_box)

        # Locate the form fields and submit button
        fullname_field = self.driver.find_element(By.ID, 'userName')
        email_field = self.driver.find_element(By.ID, 'userEmail')
        current_address_field = self.driver.find_element(By.ID, 'currentAddress')
        permanent_address_field = self.driver.find_element(By.ID, 'permanentAddress')
        submit_button = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download(self):
        # Locate the upload section, download section and the download button
        upload_download = self.driver.find_element(By.ID, 'item-7')
        self.driver.execute_script("arguments[0].click();", upload_download)
        download_button = self.driver.find_element(By.ID, 'downloadButton')
        self.driver.execute_script("arguments[0].click();", download_button)

    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login('okayuokay5', 'A1b@cDef')
    webautomation.fill_form("James Fur", "jamesfur@gmail.com",
                            "James street 50, Texas, USA",
                            "James street 50, Texas, USA")
    webautomation.download()
    webautomation.close()


