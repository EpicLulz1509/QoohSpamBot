from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.headless = True

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe", options=chromeOptions)
chromeOptions = webdriver.ChromeOptions()
driver.set_window_size(1024, 600)
driver.maximize_window()

link = "http://m.qooh.me"           #link of person you want to spam
i = 0
driver.get(link)
while(i < 100):
    time.sleep(1)
    text = driver.find_element_by_xpath("//*[@id='question']")
    text.send_keys(f"This is a bot. Apologies in advance for the spam but this is too much fun. {i}")
    driver.find_element_by_xpath("//*[@id='designed-textarea-send-btn']").click()
    time.sleep(1)
    driver.get(link)
    print(f"Success {i}")
    i = i + 1