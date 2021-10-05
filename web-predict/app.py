# $pip install Flask

# GET 요청 = 어떤 내용을 표시할지 요청
# POST 요청 = 사용자가 form을 입력 후 양식 제출

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm  # 회원가입 form 호출

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'  # 웹 애플리케이션 공격으로부터 보호


########################### web-predict ####################################
@app.route('/')
def main():
    return render_template("base_predict.html")
############################################################################


# 각 학생들에 대한 딕셔너리 선언
student_data = {
    1: {"name": "김철수", "score": {"국어": 90, "수학": 65}},
    2: {"name": "김영희", "score": {"국어": 75, "영어": 80, "수학": 75}}
}

# 고정된 URL을 view 함수에 바인딩하는 과정 - route() 데코레이터 사용
# 1. 웹 브라우저에서 URL을 방문
# 2. 서버에 요청을 보냄
# 3. 서버는 요청을 처리해서 브라우저에 응답을 반환함
# 4. 반환된 결과를 HTML 문서로 보내주면 그 웹 페이지를 브라우저가 띄워주는 것
#@app.route('/')
@app.route('/score')
def score():
    return render_template("index.html", template_students=student_data)  # 템플릿 렌더링해서 URL에 연결


@app.route("/student/<int:id>")
def student(id):
    return render_template("student.html",
            template_name=student_data[id]["name"],
            template_score=student_data[id]["score"])


# 동적 URL 다루는 방법
# 1. URL은 문자열임
# 2. <converter : variable_name> 구문을 사용해서 URL에서 받은 변수 타입을 변형할 수 있음
@app.route('/user/<user_name>/<int:user_id>')
def user(user_name, user_id):
    return 'Hello, {0}({1})!'.format(user_name, user_id)


@app.route('/home')
def home():
    #return "안녕하세요"
    return render_template('layout.html')


@app.route('/register', methods=["GET", "POST"])
def register():  # 회원가입 URL
    form = RegistrationForm()  # 인스턴스 생성
    if form.validate_on_submit():  # 'POST 요청을 통한 form 제출 O' & 'GET 요청 O' -> 회원가입 templates 반환 및 로그인 결과 전달
        # 알람 카테고리에 따라 부트스트랩에서 다른 스타일을 적용 (success, danger)
        flash(f'{form.username.data} 님 가입 완료!', 'success')  # flash = 부트스트랩을 사용한 알림 메시지 호출
        return redirect(url_for('home'))  # redirect url_for() 안에 view 함수 이름 대입
    return render_template('register.html', form=form)  # 'POST 요청을 통한 form 제출 X' & 'GET 요청 O' -> 회원가입 templates 반환


if __name__ == '__main__':
    app.run(debug=True)  # 파일의 코드를 수정할 때마다 Flask가 변경된 것을 인식하고 다시 시작