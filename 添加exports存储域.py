# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Test_cDesktop import Test_cDesktop

url = "https://192.168.8.170/mcvdi-center/"
# exports存储域参数
name = "exports"
storage = "Export / NFS"
exports_path = "192.168.8.240:/mnt/hdd/datadomain/exports"

driver = webdriver.Firefox()
test_df = Test_cDesktop(driver, url)
test_df.login(driver, url)
print "登录成功!"

# 定位到存储
driver.find_element_by_xpath(
    "html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[5]/a/div[3]/div").click()
WebDriverWait(driver, 5).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='MainTabStorageView_table_NewDomain']"))
print "打开存储页面"

test_df.add_storage(driver, name, storage, exports_path)

# 关闭浏览器
test_df.teardown(driver)
