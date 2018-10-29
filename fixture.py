import  unittest
from selenium import webdriver
import time,os

class fixture(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://127.0.0.1:8000/index")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() #close()关闭当前窗口，quit()关闭所有关联窗口
    '''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/index")
    def tearDown(self):
        self.driver.quit()     #close()关闭当前窗口，quit()关闭所有关联窗口
    '''
    def sign(self,username,password1,password2,email,sex):
        self.driver.find_element_by_css_selector('#sign1').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#username1').clear()
        self.driver.find_element_by_css_selector('#username1').send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#password1').clear()
        self.driver.find_element_by_css_selector('#password1').send_keys(password1)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#password2').clear()
        self.driver.find_element_by_css_selector('#password2').send_keys(password2)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#email').clear()
        self.driver.find_element_by_css_selector('#email').send_keys(email)
        time.sleep(1)
        #self.driver.find_element_by_css_selector('#sex').clear()  #select控件不能clear,运行报错
        self.driver.find_element_by_css_selector("#sex").send_keys(sex)
        time.sleep(2)
        self.driver.find_element_by_css_selector('#sign2').click()


    def login(self,username,password):
        self.driver.find_element_by_css_selector('#login').click()
        self.driver.find_element_by_css_selector('#username1').clear()
        self.driver.find_element_by_css_selector('#username1').send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#password1').clear()
        self.driver.find_element_by_css_selector('#password1').send_keys(password1)
        time.sleep(1)
        self.driver.find_element_by_css_selector('#login').click()

