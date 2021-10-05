# 1. form을 활용하기 위한 클래스를 담아놓는 파일
# 2. 이후 flask 앱에서 미리 생성해놓은 form 클래스를 가져다 쓰면 됨

# form을 만들기 위해 FlaskForm 부모클래스 import
from flask_wtf import FlaskForm
# wtforms 라이브러리
# -> StringField(문자열), PaswordField(패스워드), SubmitFields(제출버튼)
from wtforms import StringField, PasswordField, SubmitField
# wtforms.validators 유효성 검사 라이브러리
# -> DataRequired(필수입력값여부), Length(길이제한), Email(이메일인지), EqualTo(이미 입력한 값과 같은 값을 입력했는지)
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):  # 자식클래스(부모클래스)
    username = StringField("아이디",
                            validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField("이메일",
                            validators=[DataRequired(), Email()])
    password = PasswordField("비밀번호",
                            validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField("비밀번호 확인",
                            validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("가입")