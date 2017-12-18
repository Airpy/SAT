# -*- coding: utf-8 -*-

"""
  @desc: page object测试基类
  @author: Amio_
  @file: base_page.py
  @date: 2017/12/18 12:01
"""
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from sat import settings


class BasePage(object):
    def __init__(self, driver, url):
        self._driver = driver
        self._url = url

    def open(self, page_title=None):
        """
        打开指定网页
        :param page_title: 网页title, 不必填
        :return: 若传入的page_title与网页title不同则触发断言
        """
        self._driver.maximize_window()
        self._driver.get(url=self._url)
        if page_title is not None:
            assert page_title in self._driver.title

    def find_element(self, *locator, timeout=None):
        try:
            return self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
        except (NoSuchElementException, TimeoutException):
            self._driver.quit()
            raise TimeoutException(msg='寻找元素失败, 定位方式为: {}'.format(locator))

    def send_keys(self, webElement, keys):
        webElement.clear()
        webElement.send_keys(keys)

    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver, timeout=settings.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
