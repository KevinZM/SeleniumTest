#-*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Test_cDesktop import Test_cDesktop
from Test_cDesktop import url
#登录
driver = webdriver.Firefox()
test_df = Test_cDesktop(driver, url)
test_df.login(driver,url)
print "登录成功!"

#定位到主机
driver.find_element_by_xpath("html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[3]/a/div[3]").click()
time.sleep(1)

#打开添加主机页面
driver.find_element_by_xpath(".//*[@id='MainTabHostView_table_New']/div").click()
element = WebDriverWait(driver, 5).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='HostPopupView_generalTab']"))
#输入主机相关信息
driver.find_element_by_id("HostPopupView_name").send_keys("server211")
driver.find_element_by_id("HostPopupView_host").send_keys("192.168.8.211")
driver.find_element_by_id("HostPopupView_userPassword").send_keys("rootroot")
driver.find_element_by_xpath("//span[text()='高级参数']").click()
#获取指印
driver.find_element_by_xpath("//a[text()='获取']").click()
time.sleep(2)
try:
    driver.find_element_by_id("HostPopupView_fetchResult").is_displayed()
except:
    print "获取指印失败"
else:
    print driver.find_element_by_id("HostPopupView_fetchResult").text
#点击确定
driver.find_element_by_id("HostPopupView_OnSaveFalse").click()
#电源管理忽略
driver.find_element_by_id("DefaultConfirmationPopupView_OnSaveInternalNotFromApprove").click()
element2 = WebDriverWait(driver, 20).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='MainTabHostView_table_content_col4_row0']"))
try:
    driver.find_element_by_xpath(".//*[@id='MainTabHostView_table_content_col4_row0']").is_displayed()
except:
    print "添加主机失败!"
else:
    print "添加主机成功!"

test_df.teardown(driver)
print "关闭浏览器成功!"