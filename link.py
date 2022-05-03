from selenium import webdriver
import time

for i in range(1,101):

    driver = webdriver.Chrome('C:/Drivers/WebDriver/chromedriver.exe') #Drive_Address
    driver.get('https://www.linkedin.com')
    time.sleep(2)

    #********** LOG IN *************

    username = driver.find_element_by_xpath("//input[@name='session_key']")
    password = driver.find_element_by_xpath("//input[@name='session_password']")

    username.send_keys('''<USER@EMAIL.COM>''') #User's_Email_Address
    password.send_keys('''<PASSWORD>''') #Password_For_LinkedIn
    time.sleep(2)

    submit = driver.find_element_by_xpath("//button[@type='submit']").click()

    #***************** ADD CONTACTS ***********************
    while True:

        for i in range(100,0,-1):

            driver.get(f"https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={i}")
            time.sleep(2)

            all_buttons = driver.find_elements_by_tag_name("button")
            connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

            for btn in connect_buttons:
                driver.execute_script("arguments[0].click();", btn)
                time.sleep(2)
                send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
                driver.execute_script("arguments[0].click();", send)
                close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
                driver.execute_script("arguments[0].click();", close)
                time.sleep(2)