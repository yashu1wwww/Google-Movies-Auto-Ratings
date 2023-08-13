from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import time
import random
import os

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)
time.sleep(3)
driver.get("https://www.google.com")
time.sleep(3)
search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')  
search_box.send_keys("beast tamil movie google ratings")
search_box.send_keys(Keys.RETURN)
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-FilmReview"]/div[1]/div/div/div[2]/div[2]/div/div/div/div/g-more-link/div/span[2]/span').click() #click on more reviews
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[8]/div/div[2]/span/div/g-dialog-content/div[2]/div/div[1]').click() #write a review
time.sleep(4)
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[8]/div/div[2]/span/div/div/div[2]/div[2]/div[2]/star-rating/div/div[5]').click() #click on 5th star
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[8]/div/div[2]/span/div/div/div[2]/div[3]/div[1]/textarea').send_keys("again thalapathy vijay rocks with his performance,wow what a movie")
time.sleep(4)
driver.find_element(By.CLASS_NAME, "IkxiNb").click() #post button
time.sleep(15)



