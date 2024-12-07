from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

# Define driver, options and service
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)

# Load the webpage
driver.get('https://demoqa.com/login')

# Locate username, password and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fill in username, password and click button
username_field.send_keys('okayuokay5')
password_field.send_keys('A1b@cDef')
driver.execute_script("arguments[0].click();", login_button)

# Locate the elements dropdown and text box
elements = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')
driver.execute_script("arguments[0].click();", elements)

text_box = driver.find_element(By.ID, 'item-0')
driver.execute_script("arguments[0].click();", text_box)

# Locate the form fields and submit button
fullname_field = driver.find_element(By.ID, 'userName')
email_field = driver.find_element(By.ID, 'userEmail')
current_address_field = driver.find_element(By.ID, 'currentAddress')
permanent_address_field = driver.find_element(By.ID, 'permanentAddress')
submit_button = driver.find_element(By.ID, 'submit')

# Fill in the form fields
fullname_field.send_keys("James Fur")
email_field.send_keys("jamesfur@gmail.com")
current_address_field.send_keys("James street 50, Texas, USA")
permanent_address_field.send_keys("James street 50, Texas, USA")
driver.execute_script("arguments[0].click();", submit_button)

# Locate the upload section, download section and the download button
upload_download = driver.find_element(By.ID, 'item-7')
driver.execute_script("arguments[0].click();", upload_download)
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)



input("Press enter to close the browser")
driver.quit()
