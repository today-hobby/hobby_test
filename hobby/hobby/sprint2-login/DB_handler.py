import pyrebase
import json
import os

class DBModule:
    def __init__(self):
        # 현재 이 파일(DBModule 클래스가 정의된 파일)의 절대 경로를 기준으로 auth 폴더 경로 만들기
        current_dir = os.path.dirname(os.path.abspath(__file__))
        auth_path = os.path.join(current_dir, "auth", "firebaseAuth.json")

        # firebaseAuth.json 파일 열기
        with open(auth_path, encoding="utf-8") as f:
            config = json.load(f)

        # Firebase 초기화
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def login(self, uid, pwd):
        users = self.db.child("users").get().val()
        if users is None:
            return False  # users가 없으면 로그인 실패

        try:
            userinfo = users[uid]
            if userinfo["pwd"] == pwd:
                return True
        except KeyError:
            return False  # 해당 uid가 없으면 로그인 실패

    def signin_verification(self, uid):
        users = self.db.child("users").get().val()
        if users is None:
            return True  # users가 없으면, 즉 데이터가 없으면 회원가입 가능

        for i in users:
            if uid == i:
                return False  # 이미 존재하는 uid이면 False
        return True  # 존재하지 않으면 True

    def signin(self, _id_, pwd, name, email):
        information = {
            "pwd": pwd,
            "uname": name,
            "email": email
        }
        if self.signin_verification(_id_):
            self.db.child("users").child(_id_).set(information)
            return True
        else:
            return False
        
     #여기부터 새로 추가하는 코드   

    '''def save_survey(self, uid, answers):

        try:
        # 각 문항을 개별로 저장
            for q_num, answer in answers.items():
                self.db.child("users").child(uid).child("survey_answers").child(q_num).set(answer)
        
            return True
        except Exception as e:
            print("설문 저장 오류:", e)
            return False'''
        
    def save_survey(self, uid, answers):
        try:
            print(f"Saving survey for UID: {uid}")
            print(f"Data: {answers}")
            self.db.child("users").child(uid).child("survey_answers").set(answers)
            print("Save complete!")
            return True
        except Exception as e:
            print("설문 저장 오류:", e)
            return False



    