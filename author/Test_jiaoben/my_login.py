# coding:utf-8
Date:2018/5/23  # Time:19:15
__author__= "zrl"

from author.Test_hanshu.onlinetest import Mtmy
from HTMLTestRunner import HTMLTestRunner
import unittest
import time

class Login(unittest.TestCase):
    def setUp(self):
        Mtmy().mtmy_login_onlineurl()
    def test_login0(self):
        Mtmy().login_online()
    def tearDown(self):
        Mtmy().browser_close()
if __name__ == "my_login":
    suitunit = unittest.TestSuite()
    suitunit.addTest(Login("test_login0"))
    now = time.strftime("%Y-%m-%d %H%M%S")
    filename = "D:\\untitled\\author\\Test_jiaoben\\result.html"
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title="wap每天美耶online测试报告",description="登陆测试用例：")
    runner.run(suitunit)
    fp.close()
