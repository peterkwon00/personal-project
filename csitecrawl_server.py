# -*- encoding: utf-8 -*-
from datetime import datetime

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://0.0.0.0', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbclass


@app.route('/')
def home():
    return render_template('csitecrawl_index.html')

@app.route('/class101', methods=['GET'])
def show_list():
    import json 
    from bson import json_util 
    class_list = list(db.class101.find()) 
    return json.dumps({'result':'success', 'msg': '이 요청은 GET!', 'data':class_list}, default=json_util.default)
        
@app.route('/class101', methods=['POST'])
def update():
    import crawl
    crawl.update()

if __name__ == '__main__':
       app.run('0.0.0.0',port=5000,debug=True)
