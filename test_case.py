import json

import pytest
import requests
from load_data import yaml_load

token = None


# 准备测试数据
# 假设接口文档提供的登录请求格式是 /api/login
@pytest.mark.parametrize('data', yaml_load.load('../data/user.yaml'))
def test_01(data):
    url = 'http://127.0.0.1:5000/api/login'

    # 模拟发送请求
    res = requests.post(url=url, json=data['user'])  # 假设接口文档提供的api参数格式要求/application/json，这里则需要改成json
    print(res.text)
    result = json.loads(res.text)
    # 获取token
    try:
        global token
        token = result['token']
    except:
        pass
    # 获取相应并解析判断响应;断言响应结果是否达到预期
    assert data['msg'] == result['msg']


def test_02():
    print(token)


if __name__ == '__main__':
    pytest.main(["-v", '-s'])
