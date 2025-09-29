from flask import Blueprint, request, redirect, url_for
from flask_login import current_user

from apps.app import db
from apps.board.models import Board, Reply

reply = Blueprint(
  "reply",
  __name__
)

@reply.route('/new/<board_id>', methods=['POST'])
def new_reply(board_id):
  content = request.form['content']
  reply = Reply(
    content=content, user_id=current_user.id, board_id=board_id
  )
  db.session.add(reply)
  db.session.commit()

  return redirect(url_for('board.detail', board_id=board_id))