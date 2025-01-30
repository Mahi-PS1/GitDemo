# Explicit wait -> works on particular element by creating object for the same and passing attributes 
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.implicitly_wait(7)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)

cartElements = driver.find_elements(By.XPATH,"//div[@class='products']/div") 
count = (len(cartElements))
assert count > 0 
for cartItem in cartElements:
    cartItem.find_element(By.XPATH,"div/button").click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
Wait = WebDriverWait(driver,10)
Wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))


print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

# EC.element_to_be_clickable(locator) - waits for an element to be clickable.
# EC.visibility_of_element_located(locator) - waits for an element to be visible.
# EC.presence_of_element_located(locator) - waits for an element to be present in the DOM.
# EC.text_to_be_present_in_element(locator, text) - waits for a specific text to appear in an element.
# EC.alert_is_present() - waits for an alert to be present.