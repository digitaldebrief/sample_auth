from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash

from sample_auth.ext.database import db
from sample_auth.models import User


def verify_login(user):
    """Validates user login"""
    username = user.get("username")
    password = user.get("password")
    if not username or not password:
        return False
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        return False
    if check_password_hash(existing_user.pwhash, password):
        return True
    return False


def create_user(username, password):
    """Creates a new user"""
    if User.query.filter_by(username=username).first():
        raise RuntimeError(f"{username} already exists")
    user = User(username=username, pwhash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return user


def delete_user(username):
    """Deletes user"""
    if not User.query.filter_by(username=username).first():
        raise RuntimeError(f"{username} does not exist")
    User.query.filter_by(username=username).delete()
    db.session.commit()


def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
