from flask import Blueprint, render_template, request, redirect, url_for

from apps.crud.forms import UserForm
from apps.crud.models import User
from apps.app import db

crud = Blueprint(
  "crud", # 블루프린트의 이름 지정
  __name__, # 블루프린트가 정의된 모듈명
  template_folder="templates/crud", # 해당블루프린트와 관련된 템플릿 파일이 있는 폴더
  static_folder="static" # 해당블루프린트와 관련된 정적 파일이 있는 폴더
)

@crud.route("/")
def index():
  return render_template("index.html")

@crud.route("/users/new", methods=['GET', 'POST'])
def create_user():
  form = UserForm()

  if form.validate_on_submit():
    user = User(
      username = form.username.data,
      email = form.email.data,
      password = form.password.data
    )

    # insert
    db.session.add(user)
    db.session.commit()

    return redirect( url_for('crud.users') )

  return render_template('create.html', form=form)


@crud.route('/form/test', methods=['GET', 'POST'])
def form_test():
  if request.method == 'POST':
    print(request.form.get('username'))
    print(request.form.get('email'))
    print(request.form.get('password'))

  return render_template('formtest.html')

# 회원 목록 페이지로 이동
@crud.route('/users')
def users():
  # 데이터베이스에서 전체 레코드를 꺼내오기
  # select * from users
  # users = db.session.query(User).all()
  users = User.query.all()
  
  return render_template('index.html', users=users)

@crud.route('/users/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
  form = UserForm()
  user = User.query.filter_by(id = user_id).first()

  if form.validate_on_submit():
    user.username = form.username.data
    user.email = form.email.data
    user.password = form.password.data

    db.session.add(user)
    db.session.commit()

    return redirect( url_for('crud.users') )

  return render_template('edit.html', user=user, form=form)

@crud.route('/users/<user_id>/delete', methods=['POST'])
def delete_user(user_id):
  User.query.filter_by(id=user_id).delete() # 가능
  # u2 = User.query.get(user_id).delete() -> 불가능

  # db.session.delete(user)
  db.session.commit()

  return redirect( url_for('crud.users') )