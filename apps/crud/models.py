from apps.app import db
from werkzeug.security import generate_password_hash

from datetime import datetime

class User(db.Model):
  # db에 생성되는 테이블명 지정
  __tablename__ = "users"

  # 컬럼들...
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255), index=True)
  email = db.Column(db.String(255), unique=True, index=True)
  password_hash = db.Column(db.String(255))
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

  @property
  def password(self):
    raise AttributeError("읽을 수 없음")
  
  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)