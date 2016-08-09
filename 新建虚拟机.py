# -*- coding:utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select,WebDriverWait
from Test_cDesktop import Test_cDesktop

url = "https://192.168.8.170/mcvdi-center/"
#操作系统类型
o_s = "Windows XP"
#桌面类型
desktop_type = "桌面"
#桌面名
name = "WinXP"
#ISO名字
ISO_name = "Windows XP-SP3-CN.iso"


driver = webdriver.Firefox()
test_df = Test_cDesktop(driver, url)
test_df.login(driver, url)
print "登录成功!"

# 定位到虚拟机页面,一般默认是虚拟机页面
# driver.find_element_by_xpath(
#     "html/body/div[3]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div/div[7]/a/div[3]/div").click()
element1 = WebDriverWait(driver, 5).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='MainTabVirtualMachineView_table_NewVm']/div"))
print "打开虚拟机页面"

driver.find_element_by_xpath(".//*[@id='MainTabVirtualMachineView_table_NewVm']/div").click()
WebDriverWait(driver, 10).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='VmPopupWidget_name']"))
print "打开新建虚拟机页面"

#常规
#选择操作系统类型
Select(driver.find_element_by_id("VmPopupWidget_osType")).select_by_value(o_s)
print "操作系统类型:",o_s
time.sleep(1)

#选择桌面类型
Select(driver.find_element_by_id("VmPopupWidget_vmType")).select_by_value(desktop_type)
print "桌面类型:",desktop_type
time.sleep(1)

driver.find_element_by_id("VmPopupWidget_name").send_keys(name)
print "桌面名称:",name
driver.find_element_by_id("null_nic1").click()
time.sleep(1)
driver.find_element_by_xpath(".//td[contains(text(),'mcvdimgmt')]").click()
# driver.find_element_by_partial_link_text("gwt").click()
print "网络:",driver.find_element_by_xpath(".//*[@id='null_nic1']/div[1]/input").get_attribute("value")
time.sleep(1)

#系统
driver.find_element_by_xpath(".//*[@id='VmPopupWidget']/div[1]/div[2]").click()
WebDriverWait(driver, 5).until(
    lambda drive: driver.find_element_by_id("VmPopupWidget_memSize"))

driver.find_element_by_id("VmPopupWidget_memSize").clear()
driver.find_element_by_id("VmPopupWidget_memSize").send_keys("2048")
print "内存:",driver.find_element_by_id("VmPopupWidget_memSize").get_attribute("value"),"MB"
time.sleep(1)

driver.find_element_by_id("VmPopupWidget_totalCPUCores").clear()
driver.find_element_by_id("VmPopupWidget_totalCPUCores").send_keys("2")
print "CPU:",driver.find_element_by_id("VmPopupWidget_totalCPUCores").get_attribute("value")
time.sleep(1)

#选择时区
Select(driver.find_element_by_id("VmPopupWidget_timeZone")).select_by_value("(GMT+08:00) China Standard Time")
print "时区:",driver.find_element_by_id("VmPopupWidget_timeZone").get_attribute("value")
time.sleep(1)

#引导选项
driver.find_element_by_xpath(".//*[@id='VmPopupWidget']/div[1]/div[9]").click()
WebDriverWait(driver, 5).until(
    lambda drive: driver.find_element_by_id("VmPopupWidget_firstBootDevice"))

Select(driver.find_element_by_id("VmPopupWidget_firstBootDevice")).select_by_value("CD-ROM")
print "第一启动项:",driver.find_element_by_id("VmPopupWidget_firstBootDevice").get_attribute("value")
time.sleep(1)
Select(driver.find_element_by_id("VmPopupWidget_secondBootDevice")).select_by_value("硬盘")
print "第二启动项:",driver.find_element_by_id("VmPopupWidget_secondBootDevice").get_attribute("value")
time.sleep(1)
driver.find_element_by_id("VmPopupWidget_cdAttached").click()
print "确认附加CD"
time.sleep(2)
Select(driver.find_element_by_id("VmPopupWidget_cdImage")).select_by_value(ISO_name)
print "附加CD:",ISO_name
time.sleep(1)

driver.find_element_by_id("VmPopupView_OnSave").click()
print "配置中..."
WebDriverWait(driver, 20).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='UiCommandButton_guideButton_配置虚拟磁盘']/div/table/tbody/tr/td[2]/div"))
print "配置完成!"
time.sleep(1)
driver.find_element_by_id("UiCommandButton_guideButton_配置虚拟磁盘").click()
# driver.find_element_by_xpath("//td[contains(text(),'配置虚拟磁盘')]").click()
print "开始配置虚拟机磁盘!"
WebDriverWait(driver, 5).until(
    lambda drive: driver.find_element_by_id("VmDiskPopupWidget_size"))
driver.find_element_by_id("VmDiskPopupWidget_size").send_keys("20")
print "磁盘:",driver.find_element_by_id("VmDiskPopupWidget_size").get_attribute("value"),"GB"
Select(driver.find_element_by_id("VmDiskPopupWidget_interface")).select_by_value("IDE")
print "接口:",driver.find_element_by_id("VmDiskPopupWidget_interface").get_attribute("value")
time.sleep(1)
driver.find_element_by_id("VmDiskPopupView_OnSave").click()
print "配置中..."
WebDriverWait(driver, 20).until(
    lambda drive: driver.find_element_by_xpath(".//*[@id='UiCommandButton_guideButton_添加另外一个虚拟磁盘']/div/table/tbody/tr/td[2]/div"))
print "配置完成!"
driver.find_element_by_id("GuidePopupView_Cancel").click()
print "新建虚拟机成功"

test_df.teardown(driver)



