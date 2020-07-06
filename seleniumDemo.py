from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from time import sleep

dirver = webdriver.Firefox()

dirver.get("https://www.zhihu.com")

dirver.maximize_window()
sleep(1)

# elem = dirver.find_element_by_id("username")
# elem.send_keys(userName)
# elem = dirver.find_element_by_id("password")
# elem.send_keys(pwd)
# elem = dirver.find_element_by_class_name("formsubmit_btn")
# elem.click()

print("知乎登陆成功")



