# -*- coding: utf-8 -*-
# @Author  : lidonghui
import pytest
from program.calc import Calculator


@pytest.fixture(scope="module")
def start():
    print('开始计算')
    calc = Calculator()
    # yield 关键字可以激活 fixture 的 teardown 功能
    # yield 相当于 return，返回数据可以直接跟在 yield 后面
    yield calc
    print("计算结束")