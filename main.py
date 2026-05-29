from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

#define driver, options and services
chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

download_path = os.getcwd()
prefs = {'download.default_directory': download_path}
chrome_options.add_experimental_option('prefs', prefs)

service = Service('chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options,service=service)

#load the webpage
driver.get('https://demoqa.com/login')

#locate username, password, and login button
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

#Fill in username and password and click Login button
username_field.send_keys('pythonstudent')
password_field.send_keys('PythonStudent123$')
driver.execute_script("arguments[0].click();", login_button)

#locate the elements dropdown and text box
elements = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
elements.click()

text_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-0"]/a')))
text_box.click()

#locate the form fields and submit button
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.XPATH, '//*[@id="submit"]')

#Fill in the form fields
fullname_field.send_keys('Jane Smith')
email_field.send_keys('jane@email.com')
current_address_field.send_keys('100 Main Street, New York, NY')
permanent_address_field.send_keys('100 Main Street, New York, NY')
submit_button.click()

#Locate the upload and download section and the download button
upload_download = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7'))))
upload_download.click()
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)

input("Press Enter to close the browser")
driver.quit()