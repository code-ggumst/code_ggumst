from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.codeggumst

doc = {
    'question':'다음 중 가장 빠른 물고기는?',
    'answer':'돛새치',
    'wrong_answer1':'개복치',
    'wrong_answer2':'금붕어',
    'wrong_answer3':'구피'
}
db.codeggumst.insert_one(doc)