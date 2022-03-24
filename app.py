from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.dbcodeggumst


# 메인페이지
@app.route('/')
def home():
    return render_template('startpage.html')

# 테스트 시작하기
@app.route('/start', methods=['GET'])
def start():
    return render_template('secondpage.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)