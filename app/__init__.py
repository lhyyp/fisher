from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.secure")
    app.config.from_object("app.setting")
    register_blueprint(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "web.login"

    db.create_all(app=app)
    return app
