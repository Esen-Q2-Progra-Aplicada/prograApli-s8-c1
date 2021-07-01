from flask import Blueprint

site = Blueprint("site", __name__)


@site.route("/")
def home():
    return "this is home"
