from flask import Flask, render_template, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.codeggumst

all = db.questions.find_one({'answer':'돛새치'})
print(all)