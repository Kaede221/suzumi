import os
import json
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from kaede import utils as utils

# 读取配置文件
with open('kaede/config.json', 'r', encoding='utf-8') as f:
    config = json.loads(f.read())

# 初始化
app = FastAPI()

default_database_name: str = config['db_name']
default_port: int = config['port']
default_r18: bool = config['r18']
default_proxy: str = config['proxy']
default_tag: str = ""
default_uid: str = ""
default_num: int = 1
default_keyword: str = ""

# 读取数据库
with open(default_database_name, 'r', encoding='UTF-8') as db:
    # 这里的main_data获取过来是一个数组，每一个元素都是一个对象，包含内容看文档
    main_data = json.loads(db.read())


@app.get('/')
def home_get(
        r18: bool = default_r18,
        proxy: str = default_proxy,
        tag: str = default_tag,
        uid: str = default_uid,
        keyword: str = default_keyword
):
    return RedirectResponse(utils.get_random_link(main_data, proxy, r18, tag, uid, keyword))


@app.post('/')
def home_post(
        r18: bool = default_r18,
        tag: str = default_tag,
        num: int = default_num,
        uid: str = default_uid,
        keyword: str = default_keyword
):
    return utils.get_random_json(main_data, r18, tag, num, uid, keyword)


@app.get('/direct')
def direct_get(
        r18: bool = default_r18,
        proxy: str = default_proxy,
        tag: str = default_tag,
        uid: str = default_uid,
        keyword: str = default_keyword
):
    return RedirectResponse(utils.get_random_link(main_data, proxy, r18, tag, uid, keyword))


@app.get('/json')
def json_get(
        r18: bool = default_r18,
        tag: str = default_tag,
        num: int = default_num,
        uid: str = default_uid,
        keyword: str = default_keyword
):
    return utils.get_random_json(main_data, r18, tag, num, uid, keyword)


if __name__ == '__main__':
    os.system('fastapi dev app.py')
