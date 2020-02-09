from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('shoppingmall.html')

@app.route('/order', methods=['GET'])
def order_listing():
    result = list(db.orders.find({},{'_id':0}))
    return jsonify({'result': 'success', 'orders': result})


@app.route('/order', methods=['POST'])
def order_add():
	# 1. 정보를 읽어온다 request.form[]
    u_receive = request.form['name_give']
    c_receive = request.form['count_give']
    a_receive = request.form['address_give']
    p_receive = request.form['phone_give']
    # 2. order ={}안에 합쳐준다
    order = {'username': u_receive, 'count': c_receive, 'address': a_receive,'phonenumber': p_receive}
    # 3. db에 넣어준다. db.orders.insert()
    db.orders.insert(order)
    # 4. client에 response를 보내준다
    return jsonify({'result': 'success'})



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)