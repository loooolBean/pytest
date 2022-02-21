import pytest

age = 10


# 叠加参数化
@pytest.mark.parametrize('a', [1, 2], ids=['第一条', '第二条'])
@pytest.mark.parametrize('b,c', [(11, 22), (22, 33)], ids=['第三条', '第四条'])
@pytest.mark.run(order=2)
@pytest.mark.smoke
@pytest.mark.skip
def test_01(a, b, c):
    print(a, b, c)


@pytest.mark.skipif(age > 5, reason='Bean')
def test_02(b):
    print(b)


if __name__ == '__main__':
    pytest.main(['-s', '-m', 'smoke', 'test_overlay.py'])
