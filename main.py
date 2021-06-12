#For educational purposes only.
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.headless = True

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe", options=chromeOptions)
chromeOptions = webdriver.ChromeOptions()
driver.set_window_size(1024, 600)
driver.maximize_window()

print("Enter link: ")
link = input()
print("Enter msg: ")
msg = input()
i = 0
driver.get(link)
while(i < 100):
    time.sleep(1)
    text = driver.find_element_by_xpath("//*[@id='question']")
    text.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='designed-textarea-send-btn']").click()
    time.sleep(1)
    driver.get(link)
    print(f"Success {i}")
    i = i + 1
