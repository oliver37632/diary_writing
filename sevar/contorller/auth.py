from sevar.model import session_scope
from flask import abort
from sevar.model.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token


def sigup(nick, name, password):
    with session_scope() as session:

        new_sigup = User(
            nick=nick,
            name=name,
            password=generate_password_hash(password)
        )
        session.add(new_sigup)
        session.commit()

        return {
                   "message": "success"
               }, 201



def login(nick, password):
    with session_scope() as session:
        user = session.query(User).filter(User.nick == nick)

        if not user.scalar():
            abort(409, 'user id code does not match')

        user = user.first()
        check_user_pw = check_password_hash(user.password, password)

        if not check_user_pw:
            abort(409, 'user password code does not match')

        access_expires_delta = timedelta(minutes=60)
        refresh_expires_delta = timedelta(weeks=1)

        access_token = create_access_token(expires_delta=access_expires_delta,
                                           identity=nick
                                           )
        refresh_token = create_refresh_token(expires_delta=refresh_expires_delta,
                                             identity=nick
                                             )
        return {
                   'access_token': access_token,
                   'refresh_token': refresh_token
               }, 201
