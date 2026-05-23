from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://demoqa/login')


input("Press Enter to close the browser")
driver.quit()