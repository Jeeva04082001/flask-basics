from flask import Blueprint
from .extensions import db
from .models import *

user_bp = Blueprint("user", __name__)

@user_bp.route("/add/<name>")
def add_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return "User added to Mysql"