from flask import Blueprint, render_template, request
from ..logic.person_logic import PersonLogic

site = Blueprint(
    "site",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/website/site",
)


@site.route("/")
def home():
    return render_template("index.html")


@site.route("/personMain")
def personMain():
    logic = PersonLogic()
    personList = logic.getAllPersons()
    return render_template("personMain.html", personList=personList)


@site.route("/personNew", methods=["GET", "POST"])
def personNew():
    if request.method == "GET":
        return render_template("personNew.html")
    elif request.method == "POST":
        return "personNew posted"
