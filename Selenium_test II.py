
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/inventory.html") # Test URL
time.sleep(5)

#Log in page
driver.find_element(By.ID, "user-name").send_keys("visual_user")# UserName text field
time.sleep(5)
driver.find_element(By.ID, "password").send_keys("secret_sauce")# Password text field
time.sleep(5)
driver.find_element(By.ID, "login-button").click()# Click Log in Button

# product page
time.sleep(5)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()# Click Add to Cart Button
time.sleep(5)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()# Click Add to Cart Button
time.sleep(5)
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()# Click Add to Cart Button
time.sleep(5)
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()# Click Add to Cart Button
time.sleep(5)
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()# Click Add to Cart Button
time.sleep(5)
driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()# Click Add to Cart Button
time.sleep(5)
driver.find_element(By.ID, "react-burger-menu-btn").click()# Click hamburger menu
time.sleep(5)
driver.find_element(By.ID, "logout_sidebar_link").click()# Click log out button
time.sleep(5)

