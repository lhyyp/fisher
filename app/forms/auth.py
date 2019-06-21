from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import length, NumberRange, DataRequired, Email, ValidationError

from app.models.user import User


class EmailForm(Form):
    email = StringField('电子邮件', validators=[DataRequired(), length(1, 64),
                                            Email(message='电子邮箱不符合规范')])


class RegisterForm(EmailForm):
    password = PasswordField(validators=[DataRequired(message="密码不可为空，请输入你的密码"), length(6, 16)])
    nickname = StringField(validators=[DataRequired(), length(2, 10, message="昵称至少两个字符，最多是个字符")])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("电子邮箱已被注册")


class LoginForm(EmailForm):
    password = PasswordField(validators=[DataRequired(message="密码不可为空，请输入你的密码")])
