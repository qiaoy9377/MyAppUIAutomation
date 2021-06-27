'''
功能描述：定义一个基类，初始化driver和自定义延时等待查找元素的公共方法，其他类继承该类
实现逻辑：
    1-导包
    2-定义basepage类
    3-初始化driver
    4-定义延时等待定位元素的方法
        4.1使用webdriverwait调用driver，设置等待时间和频率，调用until方法，传入要定位的元素
        4.2返回该元素
'''
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from common.logs import logger

class BasePage():

    def __init__(self,driver):
        self.driver = driver

    def by_find_element(self,*element):
        try:
            element = WebDriverWait(self.driver,10,0.5).until(expected_conditions.presence_of_element_located(element))
            return element
        except Exception as msg:
            logger.error('定位失败',msg)

    def by_find_elements(self,*element):
        try:
            element = WebDriverWait(self.driver,10,0.5).until(expected_conditions.presence_of_all_elements_located(element))
            return element
        except Exception as msg:
            logger.error('定位失败',msg)