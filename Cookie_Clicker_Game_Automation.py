from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

# Finding cookie on webpage to click on.

cookie = driver.find_element(By.XPATH, value= '//*[@id="cookie"]')

# Giving program a chance to load before clicking.

time.sleep(2)

# Setting start time as going to run program for 5 minutes to see how many cookies per second I can get to.
# Will also start buying items every 2 seconds but increasing time interval after every purchase.

time_start = time.time()
n = 1
count = 1

while time.time() < time_start + 300:
    cookie.click()
    if time.time() > time_start + ((2 + count) * n):
        number_of_cookies = driver.find_element(By.XPATH, value='//*[@id="money"]')
        number_of_cookies = int(number_of_cookies.text.replace(",",""))
        cursor = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
        grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
        factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
        mine = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
        shipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
        alc = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
        portal = driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
        time_m = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')
        store = [time_m, portal, alc, shipment, mine,factory, grandma, cursor]
        store1 = [time_m.text, portal.text, alc.text, shipment.text, mine.text,factory.text, grandma.text, cursor.text]
        lst2 = []
        string1 = ""
        for item in store1:
            for c in item:
                if c.isdigit():
                    string1 += c
            lst2.append(int(string1))
            string1 = ""
        for upgrade in lst2:
            if number_of_cookies >= upgrade:
                store[lst2.index(upgrade)].click()
                count *= 1.1
                break
        n += 1