# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
import time


class Test_cDesktop(object):
    # url = "https://192.168.8.170/mcvdi-center/"

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def login(self, driver, url):
        driver.get(url)
        print "打开初始页"
        elem = driver.find_element_by_xpath("//*[@id='dynamicLinksSection']/div/div[1]/a[4]/div")
        elem.click()
        print "打开主页"
        driver.switch_to_window(driver.window_handles[-1])
        driver.maximize_window()
        print "最大化"
        print driver.current_url
        print driver.title
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("LoginPopupView_userName"))
        driver.find_element_by_id("LoginPopupView_userName").send_keys("sysadmin")
        driver.find_element_by_id("LoginPopupView_password").send_keys("admin==1")
        driver.find_element_by_id("LoginPopupView_loginButton").click()
        WebDriverWait(driver, 50).until(
            lambda drive: driver.find_element_by_id("SearchPanelView_searchStringInput"))
        time.sleep(2)
        print "*" * 40
        print "登录" + url
        print "*" * 40

    def add_storage(self, driver, name, storage, path):

        # 打开新建存储页面
        driver.find_element_by_id("MainTabStorageView_table_NewDomain").click()
        WebDriverWait(driver, 5).until(
            lambda drive: driver.find_element_by_xpath(".//*[@id='StoragePopupView_name']"))
        print "打开新建存储页面"

        # 创建存储域
        driver.find_element_by_id("StoragePopupView_name").send_keys(name)
        Select(driver.find_element_by_id("StoragePopupView_availableStorageItems")).select_by_value(storage)
        time.sleep(1)
        driver.find_element_by_id("NfsStorageView_pathEditor").send_keys(path)
        driver.find_element_by_id("StoragePopupView_OnSave").click()
        # 等待创建成功
        WebDriverWait(driver, 10).until(
            lambda drive: driver.find_element_by_xpath(".//*[@id='MainTabStorageView_table_content_col1_row0']"))
        time.sleep(5)
        # 验证
        a = 60
        while a > 0:

            element = driver.find_element_by_xpath(".//*[@id='MainTabStorageView_table_content_col6_row0']").text
            if element == "Active":
                print "添加",name,"存储域成功!"
                break
            else:
                print "*" * 16, "识别中", "*" * 16
                time.sleep(1)
                a = a - 1

        if a <= 0:
            print "添加",name,"存储域失败!(1 min)"

    def teardown(self, driver):
        driver.quit()
        print "*" * 40
        print "关闭浏览器!"
        print "*" * 40

    def logout(self, driver):
        driver.find_element_by_xpath("//*[@id='HeaderView_logoutLink']").click()
        print "点击登出!"
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//*[@id='LoginPopupView_userName']").is_displayed()
        except:
            print "未找到元素"
            a = False
        else:
            print "元素存在"
            a = True
        if a == True:
            print "*" * 40
            print "退出登录"
            print "*" * 40
        else:
            print "退出登录失败!"


if __name__ == "__main__":
    url = "https://192.168.8.170/mcvdi-center/"
    driver = webdriver.Firefox()
    df = Test_cDesktop(driver, url)
    df.login(driver, url)
    time.sleep(1)
    df.logout(driver)
    time.sleep(1)
    df.teardown(driver)

    print "*" * 40
    print "测试结束!"
    print "*" * 40
