'''
功能描述：执行首页测试操作，断言测试结果
实现逻辑：
    1-导包：unittest
    2-调用driver模块的driver
    3-定位功能元素，进行功能操作
    4-断言操作结果
'''

import unittest,time,os
from common.myTest import Mytest
from selenium.webdriver.common.by import By
from common.readExcel import ReadExcel
from common.logs import logger
from PO.homePage import HomePage

class HomeTest(Mytest):

    re = ReadExcel()
    @unittest.skip
    def test_send_little_message(self):
        class_name = self.__class__.__name__
        method_name = self._testMethodName
        test_data = self.re.getData(class_name,method_name)
        try:
            time.sleep(5)
            # self.driver.find_element(By.ID,'com.ss.android.article.news:id/bov').click()
            # time.sleep(2)
            # relese_list = self.driver.find_elements(By.CLASS_NAME,'android.widget.LinearLayout')
            # relese_list[0].click()
            # time.sleep(2)
            # self.driver.find_element(By.ID,'com.ss.android.article.news:id/blh').send_keys(test_data)
            # time.sleep(1)
            # self.driver.find_element(By.ID,'com.ss.android.article.news:id/a8n').click()
            hp = HomePage(self.driver)
            hp.sendLittleMsg(test_data)
            time.sleep(2)
            assert str(self.driver.page_source).find('我爱学python') != -1, print('发布失败')
        except Exception as msg:
            logger.error('执行异常',msg)
            raise
    @unittest.skip
    def test_search_nomal(self):
        class_name = self.__class__.__name__
        method_name = self._testMethodName
        test_data = self.re.getData(class_name,method_name)
        logger.debug(test_data)
        try:
            time.sleep(5)
            # self.driver.find_element(By.ID,'com.ss.android.article.news:id/bo_').click()
            # time.sleep(1)
            # self.driver.find_element(By.ID,'com.ss.android.article.news:id/vr').send_keys(test_data)
            # time.sleep(1)
            # self.driver.find_element(By.ID,'com.ss.android.article.news:id/fn').click()
            hp = HomePage(self.driver)
            hp.homeSearch(test_data)
            time.sleep(1)
            assert str(self.driver.page_source).find('孙一宁') != -1,print('断言失败')
        except Exception as msg:
            logger.error('执行异常',msg)

    def test_search_abnomal(self):
        try:
            time.sleep(5)
            # self.driver.find_element(By.ID, 'com.ss.android.article.news:id/bo_').click()
            # time.sleep(1)
            # self.driver.find_element(By.ID, 'com.ss.android.article.news:id/acg').click()
            hp = HomePage(self.driver)
            hp.searchTextClick()
            hp.searchBack()
            time.sleep(2)
            assert str(self.driver.page_source).find('发布') != -1, print('断言失败')
        except Exception as msg:
            logger.error('执行异常', msg)

if __name__ == '__main__':
    unittest.main()