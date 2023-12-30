from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config') # имя файла/имя класса

    db.init_app(app)
    migrate.init_app(app=app, db=db)
    csrf.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes

        return app


