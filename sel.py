from selenium import webdriver
from selenium.webdriver.support import select
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://nstu.ru/")
time.sleep(10)
browser.find_element("xpath", "/html/body/div[2]/header/div[1]/div[2]/div[2]/div[2]/nav/div[1]/a").click()
time.sleep(3)
browser.find_element("xpath", "/html/body/div[2]/div/main/div[4]/a[8]").click()
time.sleep(3)
browser.find_element("xpath", "/html/body/div[2]/div/main/div[4]/div[1]/a").click()
time.sleep(3)
browser.find_element("xpath", "/html/body/div[2]/div/main/div[4]/div[1]/div/div[4]/div[4]/a").click()
time.sleep(3)
browser.find_element("xpath", "/html/body/div[2]/div/main/div[8]/a[3]").click()
time.sleep(3)
print(browser.current_window_handle)
browser.switch_to.window(browser.window_handles[1])
print(browser.current_window_handle)
time.sleep(3)
for i in range(2, 102):
    info = browser.find_element("xpath", f"/html/body/div[2]/div/main/div[10]/div[2]/div[{i}]")
    print(f"{info.text}")
browser.close()