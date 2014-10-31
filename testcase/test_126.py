# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from public import my_library
import xml.dom.minidom

class test_126(unittest.TestCase):
    def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.base_url = "http://mail.126.com/"
		self.verificationErrors = []
		self.accept_next_alert =True
    
    def test_login(self):
		dom=xml.dom.minidom.parse('D:\\MyGitSource\\126\\data\\info.xml')
		root=dom.documentElement
		Users=root.getElementsByTagName('login')
		for User in Users:
			username=User.getAttribute("username")
			password=User.getAttribute("password")
			driver=self.driver
			driver.get(self.base_url)
			driver.maximize_window()
			#调用login函数
			my_library.login(self,username,password)
			#断言验证用户名
			username_text=driver.find_element_by_id('spnUid').text
			self.assertEqual(username+"@126.com",username_text)
			#调用logout函数
			my_library.logout(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()

