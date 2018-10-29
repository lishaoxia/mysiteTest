import unittest
import os,time
from HTMLTestRunner import HTMLTestRunner



if __name__ == '__main__':
    path =  os.path.join(os.getcwd(),'testcase') #先获取runtest.py文件的所在目录，再拼接testcase目录
    discover = unittest.defaultTestLoader.discover(path, pattern='test_*.py' )
    now = time.strftime("%Y-%m-%d %H_%M_%S")    #时分秒中间是下划线
    # 定义测试报告名字
    report_name = os.path.join('report', 'result_'+ now + '.html')  #先拼接名称再链接report目录
    file_open = open(report_name,'wb')  #打开测试报告，没有会自动创建一个，以二进制写方式打开
    #runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(file_open,title="mysite测试报告",description='用例执行情况')
    runner.run(discover)
    file_open.close()