#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

url = "https://192.168.8.170/mcvdi-center/"

class Test_cDesktop(object):

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def login(self,driver,url):
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
        driver.find_element_by_id("LoginPopupView_userName").send_keys("sysadmin")
        driver.find_element_by_id("LoginPopupView_password").send_keys("admin==1")
        driver.find_element_by_id("LoginPopupView_loginButton").click()
        element = WebDriverWait(driver, 50).until(
            lambda drive: driver.find_element_by_id("SearchPanelView_searchStringInput"))
        time.sleep(2)
        print "*" * 40
        print "登录" + url
        print "*" * 40

    def teardown(self,driver):
        driver.quit()
        print "*" * 40
        print "关闭浏览器!"
        print "*" * 40

    def logout(self,driver):
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

    driver = webdriver.Firefox()
    df = Test_cDesktop(driver, url)
    df.login(driver,url)
    time.sleep(1)
    df.logout(driver)
    time.sleep(1)
    df.teardown(driver)

    print "*" * 40
    print "测试结束!"
    print "*" * 40
