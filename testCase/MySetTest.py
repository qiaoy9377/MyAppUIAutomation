'''
功能描述：实现我的页面的功能测试
实现逻辑：
    1-导包
    2-继承unittest方法
    3-编写以test开头的测试方法，执行测试操作
    4-断言测试结果
'''
import unittest,time

from selenium.webdriver.common.by import By
from PO.mySetPage import MySetPage
from common.myTest import Mytest

class MySetTest(Mytest):

    def test_myset_page(self):
        try:
            time.sleep(5)
            # self.driver.find_elements(By.CLASS_NAME,'android.widget.RelativeLayout')[4].click()
            msp = MySetPage(self.driver)
            msp.mySetClick()
            time.sleep(1)
            assert str(self.driver.page_source).find('常用') != -1 ,print('断言失败')
        except Exception as msg:
            print('执行错误',msg)

    def test_myset_page_message(self):
        try:
            time.sleep(5)
            # self.driver.find_elements(By.CLASS_NAME,'android.widget.RelativeLayout')[4].click()
            # time.sleep(1)
            # self.driver.find_elements(By.CLASS_NAME,'android.widget.RelativeLayout')[0].click()
            msp = MySetPage(self.driver)
            msp.mySetClick()
            msp.myCreat()
            time.sleep(2)
            assert str(self.driver.page_source).find('内容审核通知') != -1 ,print('断言失败')
        except Exception as msg:
            print('执行错误',msg)

if __name__ == '__main__':
    unittest.main()