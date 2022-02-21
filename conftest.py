# def pytest_collection_modifytimes(items):
#     # 测试用例手机完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode_escape')
#         print(item.nodeid)
#         item._nodeid = item.nodeid.encode('utf-8').decode('inicode_escape')