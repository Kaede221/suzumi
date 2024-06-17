from flask import Flask, request, redirect, jsonify
import json
import yaml
import utils as utils

# 初始化，可以后期在这里修改
app = Flask(__name__)

# 读取配置文件
with open('config.yaml', 'r', encoding='UTF-8') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

default_database_name = config['database_name']
default_port = config['port']
default_r18 = config['r18']
default_proxy = config['proxy']
default_tag = None
default_uid = None
default_num = 1
default_keyword = None

# 可以修改数据库名称
with open(default_database_name, 'r', encoding='UTF-8') as db:
    # 这里的main_data获取过来是一个数组，每一个元素都是一个对象，包含内容看文档
    main_data = json.loads(db.read())


@app.route('/', methods=['GET', 'POST'])
def home():
    # 先判断是post还是get
    if request.method == 'GET':
        r18 = True if request.args.get('r18') is not None else default_r18
        proxy = default_proxy if request.args.get('proxy') is None else request.args.get('proxy')
        tag = request.args.get('tag') if request.args.get('tag') is not None else default_tag
        uid = request.args.get('uid') if request.args.get('uid') is not None else default_uid
        keyword = request.args.get('keyword') if request.args.get('keyword') is not None else default_keyword
        return redirect(utils.get_random_link(main_data, proxy, r18, tag, uid, keyword))
    else:
        r18 = True if request.args.get('r18') is not None else default_r18
        tag = request.args.get('tag') if request.args.get('tag') is not None else default_tag
        num = request.args.get('num') if request.args.get('num') is not None else default_num
        uid = request.args.get('uid') if request.args.get('uid') is not None else default_uid
        keyword = request.args.get('keyword') if request.args.get('keyword') is not None else default_keyword
        return jsonify(utils.get_random_json(main_data, r18, tag, num, uid, keyword))


@app.route('/direct')
def get_direct():
    r18 = True if request.args.get('r18') is not None else default_r18
    proxy = default_proxy if request.args.get('proxy') is None else request.args.get('proxy')
    tag = request.args.get('tag') if request.args.get('tag') is not None else default_tag
    uid = request.args.get('uid') if request.args.get('uid') is not None else default_uid
    keyword = request.args.get('keyword') if request.args.get('keyword') is not None else default_keyword
    return redirect(utils.get_random_link(main_data, proxy, r18, tag, uid, keyword))


@app.route('/json')
def get_json():
    r18 = True if request.args.get('r18') is not None else default_r18
    tag = request.args.get('tag') if request.args.get('tag') is not None else default_tag
    num = request.args.get('num') if request.args.get('num') is not None else default_num
    uid = request.args.get('uid') if request.args.get('uid') is not None else default_uid
    keyword = request.args.get('keyword') if request.args.get('keyword') is not None else default_keyword
    return jsonify(utils.get_random_json(main_data, r18, tag, num, uid, keyword))


if __name__ == '__main__':
    app.run(debug=True, port=default_port)
