from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.codeggumst

col = db["questions"]
dict = [
    {
        'question': '다음 중 가장 빠른 물고기는?',
        'answer': '돛새치',
        'w_answer1': '개복치',
        'w_answer2': '금붕어',
        'w_answer3': '구피',
    },
    {
        'question': '고양이 수염이 있는 이유는?',
        'answer': '주변 환경의 변화를 느끼고 감지하기 위해',
        'w_answer1': '사람의 콧수염처럼 수컷 고양이에게만 있다',
        'w_answer2': '외부 물질이 눈과 입으로 들어오는 것을 막기 위해',
        'w_answer3': '눈과 코에 먼지나 작은 입자들이 붙는 것을 막기 위해',
    },
    {
        'question': '“To be, or not to be : that is the question (죽느냐, 사느냐. 이것이 문제로다.)” 는 어느 작가가 쓴 어느 작품의 명언인가?',
        'answer': '<햄릿>, 셰익스피어',
        'w_answer1': '<동백 아가씨>, 뒤마',
        'w_answer2': '<나이팅게일과 장미>, 와일드',
        'w_answer3': '<셜록홈즈>, 코난 도일',
    },
    {
        'question': '북극성은 어떤 별자리에 속합니까?',
        'answer': '작은곰자리',
        'w_answer1': '큰곰자리',
        'w_answer2': '카시오페아자리',
        'w_answer3': '케페우스자리',
    },
    {
        'question': '세종대왕은 제 몇대 임금인가?',
        'answer': '4대',
        'w_answer1': '3대',
        'w_answer2': '7대',
        'w_answer3': '8대',
    },
    {
        'question': '18세기에서 삼각 무역은 중국, 영국과 ____ 간의 무역을 가르킨다',
        'answer': '인도',
        'w_answer1': '프랑스',
        'w_answer2': '포르투갈',
        'w_answer3': '스페인',
    },
    {
        'question': '인스턴트 라면을 최초로 개발한 나라는?',
        'answer': '일본',
        'w_answer1': '태국',
        'w_answer2': '베트남',
        'w_answer3': '중국',
    },
    {
        'question': '물 위를 걸을 수 있는 곤충은?',
        'answer': '소금쟁이',
        'w_answer1': '물방개',
        'w_answer2': '물맴이',
        'w_answer3': '게아재비',
    },
    {
        'question': '세계에서 가장 유명한 초상화인 ‘모나리자’는 다음 중 어느 곳에 전시되어 있을까?',
        'answer': '루브르 박물관',
        'w_answer1': '영국 박물관',
        'w_answer2': '오르세 미술관',
        'w_answer3': '프라도 미술관',
    },
    {
        'question': '역사상 가장 많은 올림픽 메달을 딴 선수는?',
        'answer': '마이클 펠프스',
        'w_answer1': '다카시 오노',
        'w_answer2': '비르깃 피셔',
        'w_answer3': '알렉세이 네모브',
    },
    {
        'question': '전설에 나오는 신령스러운 새이며 죽음과 부활을 반복하여 불사조라고도 불리는 이것은 무엇일까?',
        'answer': '피닉스',
        'w_answer1': '오닉스',
        'w_answer2': '파닉스',
        'w_answer3': '리눅스',
    },
    {
        'question': '한국 청동기시대의 대표적인 무덤 양식으로, 지석묘라고도 불리는 이것은 무엇일까?',
        'answer': '고인돌',
        'w_answer1': '납골묘',
        'w_answer2': '영릉',
        'w_answer3': '매장묘',
    },
    {
        'question': '“그래도 지구는 돈다”라고 말한 사람의 이름은 무엇인가?',
        'answer': '갈릴레오 갈릴레이',
        'w_answer1': '레오나르도 다빈치',
        'w_answer2': '한니발 바르카',
        'w_answer3': '아테네',
    },
    {
        'question': '소음 측정 단위로 옳은것은?',
        'answer': 'dB',
        'w_answer1': 'ppm',
        'w_answer2': 'BOD',
        'w_answer3': 'COD',
    },
    {
        'question': '세계 최초로 안락사를 합법화한 나라는?',
        'answer': '네덜란드',
        'w_answer1': '미국',
        'w_answer2': '영국',
        'w_answer3': '스위스'
    }
]

x = col.insert_many(dict)