# -*- coding: utf-8 -*-
# @Author  : lidonghui
import allure
import pytest
import yaml

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['datas']
    add_datas = datas['add']
    sub_datas = datas['sub']
    mul_datas = datas['mul']
    div_datas = datas['div']
    myid = datas['myid']


@pytest.fixture(params=add_datas, ids=myid)
def get_adddatas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


@pytest.fixture(params=sub_datas, ids=myid)
def get_subdatas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


@pytest.fixture(params=mul_datas, ids=myid)
def get_muldatas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


@pytest.fixture(params=div_datas, ids=myid)
def get_divdatas(request):
    data = request.param
    print(f"测试数据为：{data}")
    yield data


@allure.feature("测试计算器")
class TestCalc:
    @pytest.mark.first
    @pytest.mark.add
    @allure.story("测试加法")
    def test_add(self, start, get_adddatas):
        # 调用相加方法
        with allure.step("计算两个数的加法"):
            result = start.add(get_adddatas[0], get_adddatas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相加结果之后写断言
        assert result == get_adddatas[2]

    @pytest.mark.fourth
    @allure.story("测试除法")
    def test_div(self, start, get_divdatas):
        # 调用相除方法
        with allure.step("计算两个数的除法"):
            result = start.div(get_divdatas[0], get_divdatas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相除结果之后写断言
        assert result == get_divdatas[2]

    @pytest.mark.second
    @allure.story("测试减法")
    def test_sub(self, start, get_subdatas):
        # 调用相减方法
        with allure.step("计算两个数的减法"):
            result = start.sub(get_subdatas[0], get_subdatas[1])
        if isinstance(result, float):
            result = round(result, 2)
        # 得到相减结果之后写断言
        assert result == get_subdatas[2]

    @pytest.mark.third
    @allure.story("测试乘法")
    def test_mul(self, start, get_muldatas):
        # 调用相乘方法
        with allure.step("计算两个数的乘法"):
            result = start.mul(get_muldatas[0], get_muldatas[1])
        if isinstance(result, float):
            result = round(result, 2)
            # 得到相乘结果之后写断言
        assert result == get_muldatas[2]
