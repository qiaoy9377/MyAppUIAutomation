'''
功能描述：读取config.ini文件的内容，获取指定section下的option值或键值对，并返回给其他模块使用
实现逻辑：
    1-导包：configparser
    2-创建读取配置文件的类
    3-初始化类属性
        3.1配置文件路径
        3.2打开配置文件
    4-定义读取指定section和option下的value值，option默认给定为all
        4.1判断option是否输入，不输入默认为all，如果option为all
         4.1.1返回option键值对列表
         4.1.2如果输入了指定的option
         4.1.3返回指定section和option对应的value值
'''
import configparser,os

class ReadConfig():
    #初始化类属性
    def __init__(self):
        config_path = os.path.dirname(os.path.dirname(__file__))+'/config.ini'
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path,'utf-8')

    def readConfig(self,section,option = 'all'):
        try:
            if option == 'all':
                option = self.conf.items(section)
                return option
            else:
                option = self.conf.get(section,option)
                return option
        except Exception as msg:
            print('输入有误，请检查',msg)

if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.readConfig('app','deviceName'))