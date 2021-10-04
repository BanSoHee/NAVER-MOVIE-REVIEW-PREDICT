# $pip install Flask

from flask import Flask, render_template

app = Flask(__name__)

student_data = {
    1: {"name": "김철수", "score": {"국어": 90, "수학": 65}},
    2: {"name": "김영희", "score": {"국어": 75, "영어": 80, "수학": 75}}
}

# 고정된 URL을 view 함수에 바인딩하는 과정 - route() 데코레이터 사용
# 1. 웹 브라우저에서 URL을 방문
# 2. 서버에 요청을 보냄
# 3. 서버는 요청을 처리해서 브라우저에 응답을 반환함
# 4. 반환된 결과를 HTML 문서로 보내주면 그 웹 페이지를 브라우저가 띄워주는 것
@app.route('/')
@app.route('/home')
def home():
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


if __name__ == '__main__':
    app.run(debug=True)  # 파일의 코드를 수정할 때마다 Flask가 변경된 것을 인식하고 다시 시작