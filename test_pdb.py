import pytest


def test_01():
    print("success")


def test_2():
    a = 1
    assert a == 2


if __name__ == '__main__':
    pytest.main(['-s', '--pdb', 'test_pdb.py'])
