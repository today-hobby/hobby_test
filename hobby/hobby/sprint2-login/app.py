from flask import Flask, redirect, render_template, url_for, request, flash, session
from DB_handler import DBModule

app = Flask(__name__)
app.secret_key = "qiojhoidfgwnuerdsfer"

DB = DBModule()

@app.route("/")
def index():
    if "uid" in session:
        user = session["uid"]
        # 로그인된 사용자에게 홈 페이지로 리디렉션
        return redirect(url_for("home"))
    else:
        user = "Login"
        # 로그인되지 않은 사용자에게 로그인 페이지로 리디렉션
        return render_template("login.html", user=user)

@app.route("/home")
def home():
    if "uid" in session:
        user = session["uid"]
        return render_template("home.html", user=user)  # 로그인된 사용자에게 보여줄 페이지
    else:
        return redirect(url_for("login"))  # 로그인되지 않은 사용자에게 로그인 페이지로 리디렉션

@app.route("/login")
def login():
    if "uid" in session:
        return redirect(url_for("home"))  # 로그인 상태에서는 바로 home 페이지로 이동
    return render_template("login.html")

@app.route("/login_done", methods=["POST"])
def login_done():
    uid = request.form.get("id")
    pwd = request.form.get("pwd")
    mbti = DB.request_mbti(uid)
    if DB.login(uid, pwd):
        session["uid"] = uid
        session["hobby_mbti"]=mbti
        return redirect(url_for("home"))  # 로그인 후 홈 페이지로 이동
    else:
        flash("아이디가 없거나 비밀번호가 틀립니다.")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "uid" in session:
        session.pop("uid")
        session.pop("hobby_mbti")
        return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

@app.route("/signin")
def signin():
    return render_template("signin.html")

    
@app.route("/signin_done", methods=["POST"])
def signin_done():
    email = request.form.get("email")
    uid = request.form.get("id")
    pwd = request.form.get("pwd")
    name = request.form.get("name")

    if DB.signin(email=email, _id_=uid, pwd=pwd, name=name):
        print("회원가입 성공")
        return redirect(url_for("index"))
    else:
        flash("중복된 아이디입니다.", "signin_error")
        print("중복된 아이디입니다.")  # 중복된 아이디일 경우 플래시 메시지 추가
        return redirect(url_for("signin"))  # redirect를 사용하여 signin 페이지로 이동
    
   ########## #여기부터 새로 추가하는 코드 ####
    
'''@app.route("/quiz_page1")
def quiz_page1():
    if "uid" not in session:
        return redirect(url_for("login"))

    return render_template("quiz_page1.html")

@app.route("/quiz_page2", methods=["GET", "POST"])
def quiz_page2():
    if "uid" not in session:
        return redirect(url_for("login"))

    """if request.method == "POST":
        # quiz_page1에서 보낸 데이터 받기
        q1 = request.form.get("q1")
        q2 = request.form.get("q2")
        q3 = request.form.get("q3")
        q4 = request.form.get("q4")
        q5 = request.form.get("q5")
        q6 = request.form.get("q6")
        q7 = request.form.get("q7")

        # 다음 페이지로 전달하거나 세션에 저장 가능
        session["q1"] = q1
        session["q2"] = q2
        session["q3"] = q3
        session["q4"] = q4
        session["q5"] = q5
        session["q6"] = q6
        session["q7"] = q7"""
    
    return render_template("quiz_page2.html")


@app.route("/quiz_page3", methods=["GET", "POST"])
def quiz_page3():
    if "uid" not in session:
        return redirect(url_for("login"))
        
    return render_template("quiz_page3.html")




@app.route("/quiz_submit", methods=["POST"])
def quiz_submit():
    if "uid" not in session:
        return redirect(url_for("login"))

    uid = session["uid"]

    # 모든 질문의 응답값 모으기
    answers = {
        "q1": session.get("q1"),
        "q2": session.get("q2"),
        "q3": session.get("q3"),
        "q4": session.get("q4"),
        "q5": session.get("q5"),
        "q6": session.get("q6"),
        "q7": session.get("q7"),
        "q8": request.form.get("q8"),
        "q9": request.form.get("q9"),
        "q10": request.form.get("q10"),
        "q11": request.form.get("q11"),
        "q12": request.form.get("q12"),
        "q13": request.form.get("q13"),
        "q14": request.form.get("q14"),
        "q15": request.form.get("q15"),
        "q16": request.form.get("q16"),
        "q17": request.form.get("q17"),
        "q18": request.form.get("q18"),
        "q19": request.form.get("q19"),
        "q20": request.form.get("q20"),
        "q21": request.form.get("q21")
    }'''

@app.route("/quiz_page1", methods=["GET", "POST"])
def quiz_page1():
    if "uid" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        # 제출된 값만 저장 (None으로 덮어쓰지 않음)
        for i in range(1, 8):
            val = request.form.get(f"q{i}")
            if val is not None:
                session[f"q{i}"] = val

        # 백엔드 보조검증(비정상 요청 대비)
        missing = [f"q{i}" for i in range(1, 8) if not session.get(f"q{i}")]
        if missing:
            # 프론트에서 이미 막지만, 혹시 모를 경우를 대비
            flash("안 푼 문제가 있습니다")
            return render_template("quiz_page1.html")
        return redirect(url_for("quiz_page2"))

    return render_template("quiz_page1.html")


@app.route("/quiz_page2", methods=["GET", "POST"])
def quiz_page2():
    if "uid" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        for i in range(8, 15):
            val = request.form.get(f"q{i}")
            if val is not None:
                session[f"q{i}"] = val

        missing = [f"q{i}" for i in range(8, 15) if not session.get(f"q{i}")]
        if missing:
            flash("안 푼 문제가 있습니다")
            return render_template("quiz_page2.html")
        return redirect(url_for("quiz_page3"))

    return render_template("quiz_page2.html")

def count_A(start, end, answers):
        return sum(1 for i in range(start, end+1) if answers.get(f"q{i}") == "A")

def compute_hobby_mbti(answers: dict) -> str:
    """
    answers: {'q1':'A'/'B', ..., 'q21':'A'/'B'} 형태
    A가 4개 이상이면 앞글자 선택(C/M, A/P, F/R)
    """
    cm = "C" if count_A(1, 7, answers)  >= 4 else "M"
    ap = "A" if count_A(8, 14, answers) >= 4 else "P"
    fr = "F" if count_A(15, 21, answers) >= 4 else "R"
    return cm + ap + fr


@app.route("/quiz_page3", methods=["GET", "POST"])
def quiz_page3():
    if "uid" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        for i in range(15, 22):
            val = request.form.get(f"q{i}")
            if val is not None:
                session[f"q{i}"] = val

        missing = [f"q{i}" for i in range(15, 22) if not session.get(f"q{i}")]
        if missing:
            flash("안 푼 문제가 있습니다")
            return render_template("quiz_page3.html")

        # 모든 답변 dict 만들기
        answers = {f"q{str(i)}": session.get(f"q{i}") for i in range(1, 22)}

        # MBTI 계산
        mbti = compute_hobby_mbti(answers)
        session["hobby_mbti"] = mbti  # 홈에서 바로 쓰기 편하도록 세션에도 보관
        # DB 저장용 payload (mbti 포함)
        payload = {"mbti": mbti, **answers}

        if DB.save_survey(session["uid"], payload):
            flash("설문이 성공적으로 저장되었습니다", "survey_success")
        else:
            flash("설문 저장에 실패했습니다.")

        return redirect(url_for("home"))

    return render_template("quiz_page3.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")




