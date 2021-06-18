'''
功能描述：定制log等级和输出格式，返回log解释器供其他模块调试使用
实现逻辑：
    1-导包：logging
    2-定义log函数，通过basicconfig配置log等级和输出格式
    3-通过getlogger创建log解释器
    4-返回log解释器
'''
import logging

def logs():

    logging.basicConfig(level=logging.DEBUG,format=format('%(name)s-%(asctime)s-%(levelname)s-%(module)s.py-[line:%(lineno)d]-%(message)s'))
    logger = logging.getLogger('My_AppUIAutomation_test')
    return logger

logger = logs()
if __name__ == '__main__':
    logger.debug('test')