# -*- coding:utf-8 -*-
from selenium import webdriver
from Test_cDesktop import Test_cDesktop

url = "https://192.168.8.170/mcvdi-center/"

driver = webdriver.Firefox()
test_df = Test_cDesktop(driver, url)
test_df.login(driver, url)
print "登录成功!"
test_df.teardown(driver)
