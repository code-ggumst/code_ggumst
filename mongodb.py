from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.codeggumst

col = db["questions"]
dict = [
    {
        'question': '다음 중 가장 빠른 물고기는?',
        'answer1': '돛새치',
        'answer2': '개복치',
        'answer3': '금붕어',
        'answer4': '구피',
        'correct': '돛새치'
    },
    {
        'question': '고양이 수염이 있는 이유는?',
        'answer1': '주변 환경의 변화를 느끼고 감지하기 위해',
        'answer2': '사람의 콧수염처럼 수컷 고양이에게만 있다',
        'answer3': '외부 물질이 눈과 입으로 들어오는 것을 막기 위해',
        'answer4': '눈과 코에 먼지나 작은 입자들이 붙는 것을 막기 위해',
        'correct': '주변 환경의 변화를 느끼고 감지하기 위해'
    },
    {
        'question': '“To be, or not to be : that is the question (죽느냐, 사느냐. 이것이 문제로다.)” 는 어느 작가가 쓴 어느 작품의 명언인가?',
        'answer1': '<햄릿>, 셰익스피어',
        'answer2': '<동백 아가씨>, 뒤마',
        'answer3': '<나이팅게일과 장미>, 와일드',
        'answer4': '<셜록홈즈>, 코난 도일',
        'correct': '<햄릿>, 셰익스피어'
    },
    {
        'question': '북극성은 어떤 별자리에 속합니까?',
        'answer1': '작은곰자리',
        'answer2': '큰곰자리',
        'answer3': '카시오페아자리',
        'answer4': '케페우스자리',
        'correct': '작은곰자리'
    },
    {
        'question': '세종대왕은 제 몇대 임금인가?',
        'answer1': '4대',
        'answer2': '3대',
        'answer3': '7대',
        'answer4': '8대',
        'correct': '4대'
    },
    {
        'question': '18세기에서 삼각 무역은 중국, 영국과 ____ 간의 무역을 가르킨다',
        'answer1': '인도',
        'answer2': '프랑스',
        'answer3': '일본',
        'answer4': '스페인',
        'correct': '인도'
    },
    {
        'question': '인스턴트 라면을 최초로 개발한 나라는?',
        'answer1': '일본',
        'answer2': '태국',
        'answer3': '베트남',
        'answer4': '중국',
        'correct': '일본'
    },
    {
        'question': '물 위를 걸을 수 있는 곤충은?',
        'answer1': '소금쟁이',
        'answer2': '물방개',
        'answer3': '물맴이',
        'answer4': '게아재비',
        'correct': '소금쟁이'
    },
    {
        'question': '세계에서 가장 유명한 초상화인 ‘모나리자’는 다음 중 어느 곳에 전시되어 있을까?',
        'answer1': '루브르 박물관',
        'answer2': '영국 박물관',
        'answer3': '오르세 미술관',
        'answer4': '프라도 미술관',
        'correct': '루브르 박물관'
    },
    {
        'question': '역사상 가장 많은 올림픽 메달을 딴 선수는?',
        'answer1': '마이클 펠프스',
        'answer2': '다카시 오노',
        'answer3': '비르깃 피셔',
        'answer4': '알렉세이 네모브',
        'correct': '마이클 펠프스'
    },
    {
        'question': '전설에 나오는 신령스러운 새이며 죽음과 부활을 반복하여 불사조라고도 불리는 이것은 무엇일까?',
        'answer1': '피닉스',
        'answer2': '오닉스',
        'answer3': '파닉스',
        'answer4': '리눅스',
        'correct': '피닉스'
    },
    {
        'question': '한국 청동기시대의 대표적인 무덤 양식으로, 지석묘라고도 불리는 이것은 무엇일까?',
        'answer1': '고인돌',
        'answer2': '납골묘',
        'answer3': '영릉',
        'answer4': '매장묘',
        'correct': '고인돌'
    },
    {
        'question': '“그래도 지구는 돈다”라고 말한 사람의 이름은 무엇인가?',
        'answer1': '갈릴레오 갈릴레이',
        'answer2': '레오나르도 다빈치',
        'answer3': '한니발 바르카',
        'answer4': '아테네',
        'correct': '갈릴레오 갈릴레이'
    },
    {
        'question': '소음 측정 단위로 옳은것은?',
        'answer1': 'dB',
        'answer2': 'ppm',
        'answer3': 'BOD',
        'answer4': 'COD',
        'correct': 'dB'
    },
    {
        'question': '세계 최초로 안락사를 합법화한 나라는?',
        'answer1': '네덜란드',
        'answer2': '미국',
        'answer3': '영국',
        'answer4': '스위스',
        'correct': '네덜란드'
    }
]

x = col.insert_many(dict)
