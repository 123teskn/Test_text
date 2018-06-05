# coding=utf-8
Data:2018/5/23 #Time":18:44
__author__ = "zrl"
from selenium import webdriver
import time
from author.Test_shuju.Test_Data import *

class Mtmy():
    def mtmy_login_onlineurl(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(onlinetest_url)
        print("打开url成功")

    def login_online(self):
        driver.find_element_by_id(login_name).send_keys(mtmy_onlinetest_num1)
        time.sleep(2)
        driver.find_element_by_id(login_pwd).send_keys(mtmy_onlinetest_pwd1)
        time.sleep(2)
        driver.find_element_by_xpath(login_button).click()
        print("登陆成功")
        time.sleep(2)
        b = driver.find_element_by_xpath(login_text).text
        print("您的网名是：%s" %b)
        assert name_OK in b
        print("欢迎您")

    def browser_close(self):
        driver.quit()
        print('退出浏览器成功')