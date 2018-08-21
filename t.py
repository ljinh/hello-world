# -*- coding: utf-8 -*-

import unittest
from mathfunc import *
import time
import HTMLTestRunner

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_add(self):
        """Test method add(a, b)"""
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2.5, divide(5, 2))

if __name__ == '__main__':

    # unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(TestMathFunc('test_add'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # file_path = './'
    # descover = unittest.defaultTestLoader.discover(file_path, pattern='t.py')
    # runner = unittest.TextTestRunner()
    # runner.run(descover)

    
    file = './'
    discover = unittest.defaultTestLoader.discover(file, pattern='./t.py')
    now = time.strftime('%Y-%m-%d_%H-%M-%S')
    result_file = './%s_result.html' % now
    result = open(result_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream= result, title = '测试报告', description="用例执行情况如下：")
    runner.run(discover)
    result.close()