import pytest

def return_argnames():
    return [(1, 1), (2, 2), [3, 3], [4, 4]]


@pytest.mark.parametrize('a,b', return_argnames(),
                         ids=['用例一', '用例二', '用例三', '用例四'])
def test_01(a, b):
    print('\n', a, b)
