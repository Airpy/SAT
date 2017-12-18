# -*- coding: utf-8 -*-

"""
  @desc: 登录页PO
  @author: Amio_
  @file: login_page.py
  @date: 2017/12/18 12:01
"""
from selenium.webdriver.common.by import By

from sat.ui.base.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://www.douban.com/'
    USERNAME = (By.ID, 'form_email')
    PASSWORD = (By.ID, 'form_password')
    SUBMIT_BTN = (By.XPATH, "//input[@class='bn-submit']")

    def __init__(self, driver):
        super().__init__(driver=driver, url=self.URL)

    def login(self):
        self.open('豆瓣')
        self.send_keys(webElement=self.find_element(*self.USERNAME), keys='xxxxx')
        self.send_keys(webElement=self.find_element(*self.PASSWORD), keys='xxxxx')
        self.find_element(*self.SUBMIT_BTN).click()
