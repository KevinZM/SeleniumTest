#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Test_cDesktop import Test_cDesktop
from Test_cDesktop import url
from selenium.webdriver.support.ui import Select

#ISO存储域名称
name = "iso"
driver = webdriver.Firefox()
test_df = Test_cDesktop(driver, url)
test_df.login(driver,url)
print "登录成功!"

#定位到存储
driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[5]/a/div[3]/div").click()
element1 = WebDriverWait(driver, 5).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='MainTabStorageView_table_NewDomain']"))
print "打开存储页面"

#打开新建存储页面
driver.find_element_by_id("MainTabStorageView_table_NewDomain").click()
element2 = WebDriverWait(driver, 5).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='StoragePopupView_name']"))
print "打开新建存储页面"

#创建ISO数据存储
driver.find_element_by_id("StoragePopupView_name").send_keys(name)
Select(driver.find_element_by_id("StoragePopupView_availableStorageItems")).select_by_value("ISO / NFS")
driver.find_element_by_xpath(".//*[@id='NfsStorageView_pathEditor']").send_keys("192.168.8.240:/mnt/hdd/datadomain/isos")
driver.find_element_by_id("StoragePopupView_OnSave").click()
#等待创建成功
element3 = WebDriverWait(driver, 10).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='MainTabStorageView_table_content_col1_row0']"))
time.sleep(5)
#验证
element4 = driver.find_element_by_xpath(".//*[@id='MainTabStorageView_table_content_col1_row0']").text

if element4 == name:
    print "新建ISO存储域成功!"
else:
    print "新建ISO存储域失败"
#关闭浏览器
test_df.teardown(driver)
print "关闭浏览器成功!"