from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/getData")
def getData():
    return {"key": "value"}
