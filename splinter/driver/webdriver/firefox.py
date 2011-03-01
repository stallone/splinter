#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver as firefox_driver
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement

class WebDriver(BaseWebDriver):

    def __init__(self):
        self.__patch_subprocess()
        self.driver = firefox_driver()
        self.__unpatch_subprocess()

        self.element_class = WebDriverElement
