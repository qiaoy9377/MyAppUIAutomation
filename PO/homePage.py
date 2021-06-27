'''
功能描述：封装页面首页元素类，元素定位为属性，定义操作方法
实现逻辑：
    1-导包
    2-创建页面类
    3-将元素定位作为类属性
    4-定义元素操作方法
'''
from selenium.webdriver.common.by import By
from PO.basePage import BasePage
from common.driver import Driver


class HomePage(BasePage):
    publish = (By.ID, 'com.ss.android.article.news:id/bov')
    publish_little_msg = (By.ID, 'com.ss.android.article.news:id/h7')
    write_msg = (By.ID, 'com.ss.android.article.news:id/blh')
    msg_publish = (By.ID, 'com.ss.android.article.news:id/a8n')
    search_text = (By.ID, 'com.ss.android.article.news:id/bo_')
    search_msg = (By.ID, 'com.ss.android.article.news:id/vr')
    search = (By.ID, 'com.ss.android.article.news:id/vo')
    search_back = (By.ID, 'com.ss.android.article.news:id/acg')

    def publishClick(self):
        self.by_find_element(*self.publish).click()

    def publishLittleMsgClick(self):
        self.by_find_element(*self.publish_little_msg).click()

    def writeMessage(self, data):
        self.by_find_element(*self.write_msg).send_keys(data)

    def msgPublish(self):
        self.by_find_element(*self.msg_publish).click()

    def sendLittleMsg(self, data):
        self.publishClick()
        self.publishLittleMsgClick()
        self.writeMessage(data)
        self.msgPublish()

    def searchTextClick(self):
        self.by_find_element(*self.search_text).click()

    def searchMsg(self, data):
        self.by_find_element(*self.search_msg).send_keys(data)

    def searchClick(self):
        self.by_find_element(*self.search).click()

    def homeSearch(self, data):
        self.searchTextClick()
        self.searchMsg(data)
        self.searchClick()

    def searchBack(self):
        self.by_find_element(*self.search_back).click()

if __name__ == '__main__':
    d = Driver()
    driver = d.startUp()
    hp = HomePage(driver)
    hp.publishClick()
    hp.publishLittleMsgClick()