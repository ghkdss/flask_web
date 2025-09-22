from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app():
  app = Flask(__name__)

  # MySQL 연결 URI 설정
  app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:1234@localhost:3306/flaskdb',
    SQLALCHEMY_TRACK_MODIFICATIONS=False, # 변경 추적 비활성화
    SQLALCHEMY_ECHO=True, # SQL문 콘솔창에 띄워주는거
    SECRET_KEY='1234',
    WTF_CSRF_SECRET_KEY='1234'
  )

  csrf.init_app(app)
  db.init_app(app)
  Migrate(app, db)

  from apps.crud import views as crud_views

  app.register_blueprint(crud_views.crud, url_prefix='/crud')

  return app