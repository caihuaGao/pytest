# -*- coding = utf-8 -*-
# @Time: 2020/12/25 13:15
# @Author: 高才华
# @File: test_interface.py
# @Software: PyCharm
import pytest


class TestIterface:
    def test_01_interface(self,all_fixture):
        print('测试接口')
        print(str(all_fixture))
