import sys
import selenium
import csv 
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

website = 'https://www.strava.com/athlete/training'

email = input('E-Mail:  ') 
password = getpass('Password:  ')

#Login and Navigate to manual upload
driver = webdriver.Chrome()
driver.get(website)


emailElem = driver.find_element_by_id("email")
emailElem.send_keys(email)
passwordElem = driver.find_element_by_name('password')
passwordElem.send_keys(password)
signinButton = driver.find_element_by_id('login-button')
signinButton.click()
time.sleep(2)

act_to_remove = ['Yoga', 'Workout']
act = 0

dropdown = Select(driver.find_element_by_id("activity_type"))
dropdown.select_by_visible_text(act_to_remove[act])


while True:
    try:
        wait = WebDriverWait(driver,30)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/table/tbody/tr[1]/td[8]/ul/li[2]/button'))).click()
        driver.switch_to_alert().accept()
        time.sleep(1)
    except:
        driver.get(website)
        time.sleep(2)

        dropdown = Select(driver.find_element_by_id("activity_type"))
        act +=1
        act %= len(act_to_remove)
        dropdown.select_by_visible_text(act_to_remove[act])
        time.sleep(2)