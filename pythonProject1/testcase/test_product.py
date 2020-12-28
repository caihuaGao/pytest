# -*- coding = utf-8 -*-
# @Time: 2020/12/25 11:56
# @Author: 高才华
# @File: test_product.py
# @Software: PyCharm
import time
import pytest


class TestRroduct:
    age = 20
    @pytest.mark.skip(age >= 20,reason="xixi")
    def test_01_xingyao(self):
        print('测试新药1')

    @pytest.mark.usermanager
    @pytest.mark.run(order=4)
    def test_02_xingyao(self):
        print('测试新药2')

    @pytest.mark.run(order=3)
    def test_03_xingyao(self):
        print('测试新药3')

    @pytest.mark.run(order=2)
    def test_04_xingyao(self):
        print('测试新药4')

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def test_05_xingyao(self):
        print('测试新药5')