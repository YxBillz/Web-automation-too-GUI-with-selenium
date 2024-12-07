from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium. webdriver.common.by import By

# Define driver and service
service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Load the webpage
driver.get('https://demoqa.com/login')

# Locate username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

# Fill in username, password and click button
username_field.send_keys('okayuokay5')
password_field.send_keys('A1b@cDef')
login_button.click()

input("Press enter to close the browser")
driver.quit()
