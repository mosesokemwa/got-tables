from os import environ
from flask import render_template, request, current_app as app
from .services import characters_query, houses_query, api_data


CHARACTERS_ENDPOINT = "/characters/"
HOUSES_ENDPOINT = "/houses/"


@app.route("/", methods=["GET"])
def index():
    people = characters_query(f"{CHARACTERS_ENDPOINT}?page=1")
    return render_template("index.html", people=people)


@app.route("/houses", methods=["GET"])
def houses():
    h = houses_query(f"{HOUSES_ENDPOINT}?page=1")
    return render_template("houses.html", houses=h)


@app.route("/details/<id_>", methods=["GET"])
def details(id_):
    character_detail = api_data(f"{CHARACTERS_ENDPOINT}{id_}")
    print(character_detail)
    for k in character_detail:
        print(k)
    return render_template("single.html", details=character_detail, id=id_)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500