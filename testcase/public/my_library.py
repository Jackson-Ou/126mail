# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

def login(self,username,password):
	driver=self.driver
	driver.find_element_by_id('idInput').clear()
	driver.find_element_by_id('idInput').send_keys(username)
	driver.find_element_by_id('pwdInput').clear()
	driver.find_element_by_id('pwdInput').send_keys(password)
	driver.find_element_by_id('loginBtn').click()


def logout(self):
	driver=self.driver
	driver.find_element_by_id('_mail_component_33_33').click()

