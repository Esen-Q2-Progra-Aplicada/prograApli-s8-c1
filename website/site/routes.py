from flask import Blueprint, render_template

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
    return render_template("personMain.html")
