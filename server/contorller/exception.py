from functools import wraps
from sqlalchemy.exc import SQLAlchemyError
from flask import abort

from server.model import session_scope


def check_exception(func):
    with session_scope() as session:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                val = func(*args, **kwargs)
            except SQLAlchemyError as e:
                session.rollback()
                abort(418, 'database error')
            finally:
                session.close()
            return val
        return wrapper