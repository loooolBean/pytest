import pytest


# 参数被赋予两个值，函数会运行两遍
# 单个参数传递
@pytest.mark.parametrize('a', ['a', 'b'])
def test_01(a):
    print('\n', a)


# 多个参数传递
@pytest.mark.parametrize('a,b', [('aaa', 'bbb'), ('Bean', '1')])
def test_02(a, b):
    print('\n', a, b)


# 运用返回值的参数传递
def return_data():
    return [(1, 1), (2, 2)]

    # 使用函数返回值的形式传入参数值


@pytest.mark.parametrize('a,b', return_data())
@pytest.mark.smoke
def test_03(a, b):
    print('\n' + "a=%d, b=%d" % (a, b))


if __name__ == '__main__':
    pytest.main(['-s', '-m', 'smoke', 'test_param.py'])
