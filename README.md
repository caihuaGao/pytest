一句大白话总结测试: 多快好省
 多---- 并发量大
 快---- 用时短
 好---- 稳定性好
 省---- 省资源

一、pytest单元测试框架
    (1)什么是单元测试框架
       单元测试框架是指在软件开发当中，针对软件的最小单位（函数，方法）进行正确性检查测试
    (2)单元测试框架
       Java：junit和testng
       pyhton：unittest和pytest
    (3)单元测试框架主要工作
        * 测试发现：从多个文件里找到我们的测试用例
        * 测试执行：按照一定的顺序和规则去执行，并生成结果
        * 测试结果：通过断言判断预期结果和实际结果的差异
        * 测试报告：统计测试进度，耗时，通过率，生成测试报告
二、单元测试框架和自动化测试框架的关系
    (1)自动化测试框架：由一个或多个自动化测试基础模块、自动化测试管理模块、自动化测试统计模块等组成的工具集合。
    (2)自动化测试框架的作用：
        * 提高测试效率，降低维护成本
        * 减少人员干预，提高测试的准确性，增加代码的重用性
        * 核心思想是让不懂代码的人也能通过这个框架实现自动化测试
    (3)pytest单元测试框架和自动化框架的关系
        单元测试框架： 只是自动化测试框架的组成部分之一
        pom(Page Object Model)设计模式： 只是自动化测试框架的组成部分之一
    数据驱动，关键字驱动，全局配置文件封装，日志监控，selenium和requests二次封装，断言，报告邮件等
三、pytest简介
    (1)pytest是一个非常成熟的python的单元框架，比unittest更灵活
    (2)pytest可以和selenium，requests，appium，结合实现web自动化，接口自动化，app自动化。
    (3)pytest可以实现测试用例的跳过以及reruns失败重试
    (4)pytest可以和allure生成非常美观的测试报告
    (5)pytest可以和Jenkins持续集成
    (6)pytest有很多非常强大的插件，并且这些插件能够实现很多实用的操作
        pytest
        pytest-xdist 测试用例分布执行，多CPU分发
        pytest-ordering 用于改变测试用例的执行顺序
        pytest-rerunsfailures 用例失败后重跑
        pytest-html 生成HTML格式的自动化测试报告
        allure-test 用于生成美观的测试报告

        安装：放到requirements.txt中，
        通过：pip install -r requirements.txt


四、使用pytest，默认的测试用例的规则以及基础应用
    (1)模块名必须以text_开头或者以_test结尾，
    (2)测试类必须以Test开头，并且不能有init方法，
    (3) 测试方法必须以test开头

五、pytest测试用例的运行方式
    1. 主函数模式
        (1)运行所以：pytest.main(['-vs'])
        (2)指定模块：pytest.main(['-vs','./testcase/test_login.py'])
        (3)指定目录：pytest.main(['-vs','./testcase'])
        (4)通过nodeid指定用例运行：nodeid由模块名，分隔符，类名，方法名，函数名组成
            pytest.main(['-vs','./testcase/test_login.py::test_04_func'])
            pytest.main(['-vs','./testcase/test_login.py::TestLogin::test_01_baili'])
        (5)分布式：pytest.main(['-vs','./testcase','-n 3'])
        (5)失败重跑：pytest.main(['-vs','./testcase','--reruns=2'])
    2. 命令行模式
        (1)运行所以： pytest
        (2)指定模块： pytest -vs ./testcase/test_login.py
        (3)指定目录： pytest -vs ./testcase
        (4)分布式：   pytest -vs ./testcase -n 2
        (5)失败重跑   pytest -vs ./testcase --reruns 2

        参数详解：-s 表示输出调试信息，包括打印信息
            -v 详细的信息 类名 方法名 打印信息等
            -vs 两个参数一起使用
            -n 支持多线程或者分布式
            --reruns num 重跑
            -x 只要有一个用例报错 停止测试
            --maxfial=2 出现两次用例失败就停止
            -k "包含字符串的用例" 根据测试用例的部分字符串 指定用例
            --html ./report/report.html: 生成html的测试报告


    3. 通过读取pytest.ini配置文件，pytest.ini的内容如下：
        [pytest]
        # 命令行参数 多个同时使用时 用空格分开
        addopts = -vs
        # 测试用例文件夹
        testpaths = ./interface_testcase
        # 配置测试搜索的模块文件名称
        python_files = test_*.py
        # 配置测试搜索的类名
        python_classes = Test*
        # 配置测试搜索的函数名
        python_functions = test
        markers =
            smoke:冒烟用例
            usermanager:用户名管理模块
            productmanager:产品管理模块

六、 pytest执行测试用例的顺序
    unitest：ASCII的大小来绝对的执行顺序
    pytest默认从上到下
    使用mark标记可以改变执行顺序
    @pytest.mark.run(ordering=num) 改变执行顺序
七、分组执行
    smoke: 冒烟用例，分布在各个模块里
    pytest -m "smoke"
    pytest -m "somkr or 自定义字符串 or 自定义字符串"
八、pytest跳过测试用例
    (1)无条件跳过
    @pytest.mart.skip(reason="笑笑太漂亮")
    (2)有条件跳过
    @pytest.mart.skip(age<=18,reason="未成年")

九、pytest框架一些前后置的处理，常用三中种
    (1)setpu/teardown,setup_class/teardown_class
        setup: 在每个用例之前只执行一次
        teardown: 在每个用例之后只执行一次
        setup_calss: 在每个类的所有用例之前执行一次
        teardown_class: 在每个类的所有用例之后执行一次
    (2)使用@pytest.fixture()装饰器来实现部分用例的前后置
        @pytest.fixture(scope="",params="",autouse="",ids="",name="")
        scope:表示的是被pytest.fixture标记的作用域，function(默认),class,module,package/session.
        params:参数化(支持列表[],元组(),字典列表[{},{}],字典元组({},{}))
        autouse=True:自动执行，默认False
        ids:当使用参数化是，给每一个值设置一个变量名
        name:表示的是被@pytest.fixture标记的方法取一个别名，当取了别名原来的名字无法使用
    (3)通过使用conftest.py和@pytest.fixture()结合使用实现全局的前后置应用(比如：项目的全局登录，模块的全局处理)
        1）conftest.py文件是单独存放的一个夹具配置文件，名称不能更改
        2）用处可以在不同的py文件中使用同一个fixture函数
        3）原则上conftest.py需要和运行的用例放在同一层，并且不需要做任何导入操作

十、pytest结合allure-pytest插件生成allure测试报告
    (1) 安装allure  https://github.com/allure-framework/allure2
        命令安装
        mac 安装命名：brew install allure
        win 安装命令：scoop install allure 若没有安装scoop需要先安装scoop
        下载安装： 下载安装包，解压，配置环境变量
        mac https://www.jianshu.com/p/47e5bafee82d
        win https://www.cnblogs.com/strive-2020/p/12630067.html
    (2) 生成json格式的临时报告
        --alluredir ./dirname
    (3) 生成allure报告
        os.system('allure generate ./dirname -o ./report --clean')
        allure generate 固定命令
        ./dirname 临时的json格式报告的路径
        -o 输出output
        ./report 生成allure报告的路径
        --clean 清空原来的报告

