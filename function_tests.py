#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Ranxf

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):  # 1
    def setUp(self):  # 2
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)  # 9

    def tearDown(self):  # 3
        self.browser.quit()

    def test_start_list(self):  # 4
        self.browser.get("http://127.0.0.1:8000")
        self.assertIn('Django', self.browser.title)  # 5
        self.fail('完成测试')  # 6

if __name__ == '__main__':  # 7
    unittest.main()  # 8
    # unittest.main(warnings='ignore')  # 8


"""
示例代码：
代码解析：
    1、测试组织成类的形式，继承自unittest.TestCase；
    2、setUp()特殊的方法，在运行各个测试方法之前运行，这儿完成打开浏览器；
    3、tearDown()也是一个特殊的方法，在运行各个测试方法之后运行，这儿完成关闭浏览器，中间有运行错误的方法，也会运行tearDown()方法，
        除非setUp()抛出异常；
    4、测试的主要代码，单元测试中，测试方法都以test_开头；
    5、self.assertIn测试断言，'To-Do'在self.browser.title中；
    6、生成指定的错误信息，这儿提醒测试结束；
    7、调用unittest.main()启动unittest的测试运行程序，这个程序在文件中自动查找测试类NewVisitorTest()和方法test_start_list();
    8、warnings='ignore'的作用是禁止ResourceWarning异常，可以不带该参数。
    9、优化代码时添加implicitly_wait()隐式等待，Selenium经常使用的方法。在操作之前等待页面完全加载，就需要等几秒钟。
"""