# -*- coding: utf-8 -*-

"""
  @desc: 浏览器引擎
  @author: Amio_
  @file: browser_engine.py
  @date: 2017/11/19 下午4:05
"""
import os

from selenium import webdriver

from sat import settings


class BrowserEngine(object):
    CURRENT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../resource')
    CHROME_DRIVER = os.path.join(CURRENT_PATH, 'chromedriver.exe')
    FIREFOX_DRIVER = os.path.join(CURRENT_PATH, 'geckodriver.exe')
    IE_DRIVER = os.path.join(CURRENT_PATH, 'IEDriverServer.exe')

    def __init__(self, browser=None):
        if browser is None:
            self._browser_type = settings.DEFAULT_BROWSER
        else:
            self._browser_type = browser
        self._driver = None

    def init_driver(self):
        if self._browser_type.lower() == 'chrome':
            self._driver = webdriver.Chrome(executable_path=self.CHROME_DRIVER)
        elif self._browser_type.lower() == 'firefox':
            self._driver = webdriver.Firefox(executable_path=self.FIREFOX_DRIVER)
        elif self._browser_type.lower() == 'ie':
            self._driver = webdriver.Ie(executable_path=self.IE_DRIVER)
        else:
            ValueError('传入的浏览器类型错误,目前仅支持Chrome/Firefox/IE.')
        self._driver.implicitly_wait(time_to_wait=settings.UI_WAIT_TIME)
        return self._driver
