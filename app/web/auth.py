from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web
from flask import request, jsonify
from flask_login import login_user


@web.route("/register", methods=["POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return jsonify(code="200", msg="注册成功")
    else:
        return jsonify(code="-1", mag=form.errors[0])


@web.route("/login", methods=["POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            next = request.args.get("next")
            if next and next.startswith("/"):
                return jsonify(code="200", mag="登录成功", path=next)
            else:
                return jsonify(code="200", mag="登录成功")
        else:
            return jsonify(code="-1", mag="账号或密码错误")
    else:
        return jsonify(code="-1", mag=form.errors[0])
