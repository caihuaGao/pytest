# -*- coding = utf-8 -*-
# @Time: 2020/12/25 13:36
# @Author: 高才华
# @File: all.py
# @Software: PyCharm
import os
import pytest

if __name__ == '__main__':

    # 不带参数 执行全部testcase
    # pytest.main()

    # '-s' 表示输出调试信息，包括打印信息
    # pytest.main(['-s'])

    # -v 详细的信息 类名 方法名 打印信息等
    # pytest.main(['-v'])

    # -vs 详细的信息 类名 方法名 打印信息等
    # ./testcase/test_login.py 指定模块
    # pytest.main(['-vs','./testcase/test_login.py'])

    # './testcase' 指定目录
    # pytest.main(['-vs','./testcase'])

    ## 函数
    # pytest.main(['-vs', './testcase/test_login.py::test_04_func'])
    ## 方法
    # pytest.main(['-vs', './testcase/test_login.py::TestLogin::test_01_baili'])

    ## './testcase' 指定目录
    pytest.main(['-vs','./'])

    os.system('allure generate ./tempjson -o ./report --clean')