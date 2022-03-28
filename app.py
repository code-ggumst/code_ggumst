from flask import Flask, render_template, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.codeggumst


# 메인페이지
@app.route('/')
def main():
    return render_template('main.html')

# 퀴즈 시작하기
@app.route('/start')
def start():
    return render_template('start.html')

@app.route('/quiz', methods=['GET'])
def questions():
    quiz = list(db.questions.find({}, {'_id': False}))
    return jsonify({'all_questions':quiz})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)