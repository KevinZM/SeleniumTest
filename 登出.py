# -*- coding:utf-8 -*-
from selenium import webdriver
from Test_cDesktop import Test_cDesktop

driver = webdriver.Firefox()
url = "https://192.168.8.170/mcvdi-center/"

test_df = Test_cDesktop(driver, url)
test_df.login(driver, url)
print "登陆成功!"
test_df.logout(driver)
print "登出成功!"
test_df.teardown(driver)
