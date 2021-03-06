import requests
import logging
import json
import datetime
import random
import config
import ast
from config import Config


# 将 bytes 转换为 string
def _bytes_to_str(bytes_info):
    return bytes_info.decode("utf-8")


# 将 requests.get 或 post 的结果 result 获取到的信息转为由 dict 构成的 list
# 使用方法 :
# content = requests.get('http://23.106.158.242:30080/users')
# get_api_info(content)
# 注意！ API 的 json 数据的最外层必须是 list 的形式，如 [{'k':'value'}]
# 不用 list 作为最外层将不能转化成功，如 {'k':'value'}
def get_api_info(request_result):
    content_str = request_result.content.decode("utf-8")
    list_content = []
    # print("json.loads length=" + str(len(json.loads(content_str))))
    # 若 api 返回的是空值
    if json.loads(content_str) is None:
        # 返回空的 list
        return []
    # 否则对 api 信息进行处理
    else:
        for item in json.loads(content_str):
            list_content.append(item)
        # 返回处理好的 list
        return list_content


# 生成当前时间 格式为 %Y-%m-%d/%H:%M:%S
def get_current_datetime():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# 生成 4 个随机数
def generate_random_code():
    code = ''
    identifiers = config.Config.IDENTIFIERS
    for item in range(4):
        text = random.choice(identifiers)
        code += text
    return code


# Revert list-like string to list
def str_to_right_type(string):
    return ast.literal_eval(str(string))


# 将 requests.get 或 post 的结果 result 获取到的信息转为唯一的 dict 。仅用于 list 中仅有一个元素的情况。
# 使用方法 :
# content = requests.get('http://23.106.158.242:30080/users')
# get_api_info(content)
# 注意！ API 的 json 数据的最外层必须是 list 的形式，如 [{'k':'value'}]
# 不用 list 作为最外层将不能转化成功，如 {'k':'value'}
def get_api_info_first(request_result):
    content_str = request_result.content.decode("utf-8")
    list_content = []
    # print("json.loads length=" + str(len(json.loads(content_str))))
    # 若 api 返回的是空值
    if json.loads(content_str) is None:
        # 返回空的 list
        return []
    # 否则对 api 信息进行处理
    else:
        for item in json.loads(content_str):
            list_content.append(item)
        # 如果 list 内没有元素, 返回空字典
        if len(list_content) < 1:
            return {'error': 'Count over the boundary!'}
        # 如果 list 内只有唯一一个元素 返回
        elif len(list_content) == 1:
            return list_content[0]
        else:
            # 返回处理好的 list 的头个元素
            return list_content[0]


# 根据 account_id 返回账户信息
def get_account_info_by_account_id(user_id):
    account_url = 'http://' + Config.ACCOUNT_SERVICE_URL +\
                  '/api/account/account-id/' + str(user_id)
    result = requests.get(account_url)
    if result.status_code == 200:
        return get_api_info_first(result)
    else:
        return {'error': 'No such user'}


if __name__ == '__main__':
    content = requests.get('http://174.137.53.253:30500/api/competition/all-competitions')
    print(get_api_info(content))
    pass
