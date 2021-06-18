'''
功能描述：整个程序的入口，实现用例自动加载到测试套件，执行测试套件，生成测试报告，并将报告以邮件发送，多余报告自动清理功能
实现逻辑：
    1-导包
    2-创建测试套件
    3-运行测试套件，生成测试报告
    4-定义自动清理报告方法
        4.1获取报告数量，判断报告数量，是否大于3个
        4.2是，对文件按照创建时间进行排序
            4.2.1循环获取报告的创建时间
                4.2.1.1将创建时间存成列表
                4.2.1.2将报告创建时间和报告名称创建为字典
            4.2.2对文件创建时间列表进行排序
            4.2.3截取需要删除的文件列表
            4.2.4遍历要删除的文件列表
                4.2.4.1删除文件
    5-调用发送邮件模块，发送邮件

'''

import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
from common.configEmail import ConfigEmail
from common.logs import logger

cur_path = os.path.dirname(__file__)
report_path = cur_path+'/testReport/'
#创建测试套件
def creatSuite():
    suite = unittest.defaultTestLoader.discover(start_dir=cur_path +'/testCase',pattern='*.py',top_level_dir=None)
    return suite

#定义报告排序的方法
def reportSort():
    report_list = os.listdir(report_path)
    report_time_list = []
    report_time_dict = {}
    for report in report_list:
        report_time = os.path.getctime(report_path+report)
        report_time_list.append(report_time)
        report_time_dict[report_time] = report
    report_time_list.sort()
    return report_time_list,report_time_dict


# 自动清理报告
def autoClearReport():
    report_time_list,report_time_dict = reportSort()
    for report_time in report_time_list[:-3]:
        os.remove(report_path + report_time_dict[report_time])

if __name__ == '__main__':
    suite = creatSuite()
    now_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())
    r = open(report_path+f'test_report{now_time}.html','wb')
    runner = HTMLTestRunner(stream=r,title='移动端自动化测试报告',description='测试用例执行结果如下：')
    runner.run(suite)
    autoClearReport()
    report_time_list, report_time_dict = reportSort()
    ce = ConfigEmail()
    ce.sendEmail(report_time_dict[report_time_list[-1]])
    # reportSort()

