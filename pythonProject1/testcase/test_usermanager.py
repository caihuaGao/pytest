# -*- coding = utf-8 -*-
# @Time: 2020/12/28 14:04
# @Author: 高才华
# @File: test_usermanager.py
# @Software: PyCharm
import pytest

def test_user110(ch_fixture):
    print('测试用户110')
    print(str(ch_fixture))

def test_user10():
    print('测试用户10')
class TestUser1:

    def test_01_user(self):
        print('测试用户1')

    def test_02_user(self, all_fixture, ch_fixture):
        print('测试用户2')
        print(str(all_fixture))
        print(str(ch_fixture))

    def test_03_user(self):
        print('测试用户3')


class TestUser2:
    def test_04_user(self):
        print('测试用户4')

    def test_05_user(self):
        print('测试用户5')

    def test_06_user(self):
        print('测试用户6')