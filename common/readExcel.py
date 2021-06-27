'''
功能描述：读取testData的excel文件的数据，根据类名和方法名，找到测试数据并返回数据，供testCase使用
实现逻辑：
    1-导包
    2-确定文件路径，打开excel文件
    3-确定sheet页
    4-获取文件行数
    5-遍历每行数据
        5.1判断类名和方法名是否等于当前类目和方法名
        5.2如果等于，返回测试数据
'''
import xlrd,os
from common.logs import logger

class ReadExcel():

    def __init__(self):
        file_path = os.path.dirname(os.path.dirname(__file__))+'/testData/data.xls'
        re = xlrd.open_workbook(file_path)
        self.sheet = re.sheet_by_index(0)
        self.rows = self.sheet.nrows
        logger.debug(self.rows)

    def getData(self,className,methodName):
        '''
        获取测试数据的函数
        :param className: 需要查找的类名
        :param methodName: 需要查找的方法名
        :return: 符合条件返回对应的测试数据，否则返回空
        '''
        for i in range(1,self.rows):
            c_name = self.sheet.cell(i,0).value
            m_name = self.sheet.cell(i,1).value
            if c_name == className and m_name == methodName:
                testData = self.sheet.cell(i,2).value
                return testData
        else:
            return ''

if __name__ == '__main__':
    re = ReadExcel()
    print(re.getData('HomeTest','test_search_nomal'))