# -*- coding = utf-8 -*-
# @Time: 2020/12/25 11:38
# @Author: 高才华
# @File: test_login.py
# @Software: PyCharm
import time

import pytest

@pytest.mark.skip(reeson="哈哈哈")
def test_10_func():
    print("函数")

class TestLogin:
    @pytest.mark.usermanager
    @pytest.mark.smoke
    def test_01_baili(self):
        print('测试百里')
