'''
功能描述：实现上滑、下滑、左滑、右滑、获取屏幕大小等公共操作，供testCase调用
实现逻辑：
    1-导包
    2-定义获取屏幕大小的方法，返回屏幕的宽、高
    3-定义上滑方法
        3.1确定起始的坐标和滑动结束的坐标
        3.2调用swipUP方法
    4-定义下滑方法
        同3，仅调整坐标
    5-定义左滑方法
        同3，仅调整坐标
    6-定义右滑方法
        同3，仅调整坐标
'''
from common.driver import Driver
import unittest,time

class Public():

    def __init__(self):
        d = Driver()
        self.driver = d.startUp()
        time.sleep(5)

    def getSize(self):
        size = self.driver.get_window_size()
        x = size['width']
        y = size['height']
        return x,y

    def swipeUp(self):
        x,y = self.getSize()
        x1 = int(x*0.5)
        y1 = int(y*0.75)
        y2 = int(y*0.25)
        self.driver.swipe(x1,y1,x1,y2,duration=1000)

    def swipeDown(self):
        x,y = self.getSize()
        x1 = int(x*0.5)
        y1 = int(y*0.25)
        y2 = int(y*0.75)
        self.driver.swipe(x1,y1,x1,y2,duration=1000)

    def swipeLeft(self):
        x,y = self.getSize()
        x1 = int(x*0.75)
        y1 = int(y*0.5)
        x2 = int(x*0.25)
        self.driver.swipe(x1,y1,x2,y1,duration=1000)

    def swipeRight(self):
        x,y = self.getSize()
        x1 = int(x*0.25)
        y1 = int(y*0.5)
        x2 = int(x*0.75)
        self.driver.swipe(x1,y1,x2,y1,duration=1000)

if __name__ == '__main__':
    p = Public()
    print(p.getSize())
    p.swipeUp()
    p.swipeDown()
    p.swipeLeft()
    p.swipeRight()