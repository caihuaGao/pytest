# -*- coding = utf-8 -*-
# @Time: 2020/12/28 15:41
# @Author: 高才华
# @File: conftest.py
# @Software: PyCharm
import pytest

@pytest.fixture(scope='function',params=["高才华","李娜"],ids=["ch","ln"])
def ch_fixture(request):
    print("\n局部前置方法")
    yield request.param
    print("\n局部后置方法")