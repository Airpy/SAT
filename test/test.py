# -*- coding: utf-8 -*-

"""
  @desc: 测试类
  @author: Amio_
  @file: test.py
  @date: 2017/12/18 12:06
"""
from sat.ui.base.browser_engine import BrowserEngine
from sat.ui.pom.login_page import LoginPage


class Test(object):
    driver = BrowserEngine().init_driver()

    def test_login(self):
        LoginPage(driver=self.driver).login()  # 实现登录
        self.driver.quit() # 一定要退出
