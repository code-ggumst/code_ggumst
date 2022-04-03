from flask import Flask, render_template, jsonify, request

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


# 퀴즈 결과
@app.route('/result')
def result():
    return render_template('result.html')


# 퀴즈 리스트 보내기
@app.route('/quiz', methods=['GET'])
def questions():
    quiz = list(db.questions.find({}, {'_id': False}))
    return jsonify({'all_quiz': quiz})


# 정오답 체크하기
@app.route('/check', methods=['POST'])
def answer_check():
    answer_receive = request.form['answer_click']
    target_question = db.questions.find_one({'correct':answer_receive})
    if target_question:
        return jsonify({'msg': 1 })
    else:
        return jsonify({'msg': 0 })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
