'''
功能描述：封装我的设置页面类
实现逻辑：
    1-导包
    2-创建我的设置页面类
    3-将元素定位作为类属性
    4-将元素操作定义为方法
'''
import time

from selenium.webdriver.common.by import By
from common.driver import Driver
from PO.basePage import BasePage

class MySetPage(BasePage):

    my_set = 'new UiSelector().text("我的")'
    my_create = (By.ID,'com.ss.android.article.news:id/cf8')

    def mySetClick(self):
        self.driver.find_element_by_android_uiautomator(self.my_set).click()

    def myCreat(self):
        self.by_find_elements(*self.my_create)[0].click()

if __name__ == '__main__':
    d = Driver()
    driver = d.startUp()
    msp = MySetPage(driver)
    msp.mySetClick()
    msp.myCreat()