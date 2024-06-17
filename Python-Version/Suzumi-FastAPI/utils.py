"""
在这里实现一些需要的方法
"""
from urllib import parse
import random
import json

import app


def use_proxy(origin_url: str, proxy: str) -> str:
    """
    运用代理地址
    :param origin_url: 初始地址，修改前的url地址，必须是完整的链接地址
    :param proxy: 需要的代理地址，必须包含https://前缀
    :return: 修改后的地址
    """
    return f"{proxy}{parse.urlparse(origin_url).path}"


def get_random_integer(minimum: int, maximum: int) -> int:
    """
    获取一个包含最小值，不包含最大值区间内的随机整数
    :param minimum: 最小值
    :param maximum: 最大值
    :return: 随机数
    """
    return random.randint(minimum, maximum - 1)


def have_intersection(l1: list, l2: list) -> bool:
    """
    判断两个列表是否相交
    :param l1: 第一个列表
    :param l2: 第二个列表
    :return: 是否
    """
    return bool(set(l1).intersection(set(l2)))


def data_filter(data: dict, r18: bool, tag: str, uid: str, keyword: str):
    """
    筛选器，对数据进行筛选
    :param data: 标准格式的data文件（具体格式请看文档）
    :param r18: 是否为r18内容 默认为0
    :param tag: 是否有tag，没有就是没有
    :param uid: 作者的id
    :param keyword: 可以查找作品名称中，tags中的关键字
    :return: False为不符合需求，否则返回原data
    """
    if (
            (data['r18'] is r18) and
            (tag == "" or have_intersection(data['tags'], tag.split('|'))) and
            (uid == "" or int(data['uid']) is uid) and
            (
                    (keyword == "") or
                    (keyword in data['tags']) or
                    (keyword in data['title'])
            )
    ):
        return True
    return False


def get_random_link(data: list, proxy: str, r18: bool, tag: str, uid: str, keyword: str) -> str:
    """
    获取一个随机的链接
    :param data: 元数据，就是那个文件直接读取的结果
    :param proxy: 代理地址
    :param r18: 是否为r18
    :param tag: tag
    :param uid: uid
    :param keyword: 关键词
    :return: 符合要求，且修改后的链接
    """
    # 创建一个新列表，用于储存满足条件的链接
    url_list = []
    for i in data:
        if data_filter(i, r18, tag, uid, keyword):
            url_list.append(i['url'])

    # 判断是否为空
    if len(url_list) == 0:
        return '404.html'

    return use_proxy(url_list[get_random_integer(0, len(url_list))], proxy)


def get_random_json(data: list, r18: bool, tag: str, num: int, uid: str, keyword: str):
    # 判断请求的数量
    if not 20 >= num >= 1:
        return []
    # 创建空列表
    data_list = []

    # 筛选数据
    for i in data:
        if data_filter(i, r18, tag, uid, keyword):
            data_list.append(i)

    # 再建立一个列表，用来储存
    final_list = []
    for i in range(num):
        final_list.append(data_list[get_random_integer(0, len(data_list))])

    # 返回即可
    return final_list


if __name__ == '__main__':
    with open('test.json', 'r', encoding='UTF-8') as db:
        # 这里的main_data获取过来是一个数组，每一个元素都是一个对象，包含内容看文档
        main_data = json.loads(db.read())
    print(get_random_json(main_data, app.default_r18, app.default_tag, app.default_num, app.default_uid,
                          app.default_keyword))
