'''
功能描述：继承unittest测试框架，创建启动app、关闭app发类，teatCase继承该类，避免app的重复启动
实现逻辑：
    1-导包-unittest
    2-创建mytest类
    3-重写setupclass、setup、teardown、teardowmclass方法
'''
import unittest
from common.driver import Driver

class Mytest(unittest.TestCase):

    # 实例化app启动类，调用启动app函数
    d = Driver()
    driver = d.startUp()

    @classmethod
    def setUpClass(cls) -> None:
        pass


    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

if __name__ == '__main__':
    mt = Mytest()
    mt.setUpClass()
    mt.tearDownClass()