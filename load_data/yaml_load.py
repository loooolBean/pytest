import yaml

# yaml格式格式内容的数据读取
def load(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FulllLoader)
    return data
