# -*- coding: utf-8 -*-
import unittest, time
import HTMLTestRunner
import sys
sys.path.append("\testcase")
from testcase import test_126



now=time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(test_126.test_126))
filename="D:\\MyGitSource\\126\\report\\report_"+now+".html"
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
runner.run(testunit)
fp.close()
print 'Report:'+'D:\\MyGitSource\\126\\report\\report_'+now+'.html'
