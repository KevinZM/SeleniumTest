#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from Test_cDesktop import Test_cDesktop
from Test_cDesktop import url

driver = webdriver.Firefox()
test_df = Test_cDesktop(driver, url)
test_df.login(driver,url)
print "登录成功!"
test_df.teardown(driver)
print "关闭浏览器成功!"
