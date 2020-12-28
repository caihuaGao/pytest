# -*- coding = utf-8 -*-
# @Time: 2020/12/28 15:33
# @Author: 高才华
# @File: conftest.py
# @Software: PyCharm
import pytest

@pytest.fixture(scope='function',params=["gg","mm"],ids=["ch","ln"])
def all_fixture(request):
    print("\n全局前置方法")
    yield request.param
    print("\n全局后置方法")