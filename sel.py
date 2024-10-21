from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://nstu.ru/")
time.sleep(5)