import fixture
import time,os,csv
from itertools import islice
#from selenium.common.exceptions import NoSuchElementException

#获取工程目录
# root_path = os.path.dirname(os.path.dirname(os.getcwd())) #先获取当前目录，再获取当前目录的父目录的父目录
'''因为此文件被runtest.py文件调用，所以在执行os.getcwd()方法时，获取的不是当前py文件的目录，而是当前运行文件
runtest.py所在的目录.所以上面注释代码获取的文件路径不正确'''
root_path = os.getcwd()
#base_path = os.path.dirname(root_path)
#测试用例方法test_开头
class sign(fixture.fixture):
    '''测试注册'''
    def test_sign_user(self):   #正常注册用户
        '''正常注册'''
        user_data = os.path.join(root_path, 'testdata', 'user_data.csv')
        users = csv.reader(open(user_data,'r'))
        for (username,passwd1,passwd2,email,sex) in islice(users,1,None):   #islice 分片 从第2行到最后，行数从0开始
            print(username,passwd1,passwd2,email,sex)
            self.sign(username,passwd1,passwd1,email,sex)
            self.assertEqual(self.driver.find_element_by_css_selector('#message_assert').text,'注册成功！')
            time.sleep(1)



    def test_sign_user_exsit(self):
        '''用户名已存在'''
        self.sign('test3','passwd1','passwd3','test1@163.com','女')
        self.assertEqual(self.driver.find_element_by_css_selector('#message').text,'用户已经存在，请重新选择用户名！')
        time.sleep(1)
