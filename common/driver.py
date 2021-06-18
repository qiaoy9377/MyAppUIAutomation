'''
功能描述：封装启动APP的方法，供其他模块调用
实现逻辑：
    1-导包
    2-创建driver类
    3-初始化启动app的属性，可以将属性通过配置文件管理
    4-启动app
    5-返回driver
'''
from appium import webdriver
from common.readConfig import ReadConfig

class Driver():

    def __init__(self):
        self.rc = ReadConfig()
        self.desire_caps = {
            'deviceName' : self.rc.readConfig('app','deviceName'),
            'platformName':self.rc.readConfig('app','platformName'),
            'platformVersion':self.rc.readConfig('app','platformVersion'),
            'appPackage':self.rc.readConfig('app','appPackage'),
            'appActivity':self.rc.readConfig('app','appActivity'),
            'noReset':bool(self.rc.readConfig('app','noReset')),  #获取到的为字符串，强制转换为bool型
            'unicodeKeyboard':bool(self.rc.readConfig('app','unicodeKeyboard'))
        }

    def startUp(self):
        driver = webdriver.Remote(self.rc.readConfig('app','remoteUrl'),self.desire_caps)
        return driver

if __name__ == '__main__':
    d = Driver()
    driver = d.startUp()