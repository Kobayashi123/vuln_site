#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SSRF脆弱性プログラム：SSRF脆弱性検証用のWebアプリケーションです。
"""

__author__ = 'kobayashi shun'
__version__ = '0.0.0'
__date__ = '2023/05/06 (Created: 2023/05/06)'

from io import BytesIO
import os
import sys

from flask import (
    jsonify,
    Flask,
    request,
    redirect,
    render_template,
    render_template_string,
)
import pycurl
import redis

app = Flask(__name__)
redis = redis.Redis(host='redis', port=6379, db=0)

@app.route('/', methods=['GET'])
def route_index():
    return render_template("index.html", data=None)

@app.route('/', methods=['POST'])
def route_index_post():
    url = request.form.get('url')

    redis.lpush('history', url)

    buf = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buf)
    c.perform()
    c.close()

    body = buf.getvalue().decode('UTF-8')
    return render_template('index.html', url=url, data=body)

@app.route('/redis', methods=['GET'])
def root_redis():
    if request.remote_addr != '127.0.0.1':
        return 'Frobidden :(', 403

    key = request.args.get('key')
    if key == '' or key == None:
        return 'key must be specified'

    if redis.exists(key) == False:
        return 'key not found'

    t = redis.type(key)

    if t == b'string':
        value = redis.get(key)
    elif t == b'list':
        value = '\n'.join([i.decode() for i in redis.lrange(key, 0, -1)])
    else:
        value = 'the type of the value is neither string or list :('

    return value

def init_flag():
    flag = os.environ['FLAG']
    redis.set('FLAG', flag)

init_flag()
app.run(host='0.0.0.0', port=5000, debug=False)

# def main():
#     """
#     Pythonファイルを生成するメイン（main）プログラムです。
#     常に0を応答します。それが結果（リターンコード：終了ステータス）になることを想定しています。
#     """

# if __name__ == '__main__':  # このスクリプトファイルが直接実行されたときだけ、以下の部分を実行する。
#     sys.exit(main())
