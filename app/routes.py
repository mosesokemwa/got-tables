from os import environ
from flask import render_template, request, current_app as app
from .services import characters_query, houses_query, api_data, books_query

CHARACTERS_ENDPOINT = "/characters"
HOUSES_ENDPOINT = "/houses"
BOOKS_ENDPOINT="/books"


@app.route("/characters", methods=["GET"])
def characters():
    params =''
    prev=False
    if request.query_string:
        params = request.query_string.decode()
        prev=True
    people = characters_query(f"{CHARACTERS_ENDPOINT}?page=1&{params}")
    return render_template("characters.html", people=people, prev=prev)


@app.route("/houses", methods=["GET"])
def houses():
    params =''
    prev=False
    if request.query_string:
        params = request.query_string.decode()
        prev=True
    h = houses_query(f"{HOUSES_ENDPOINT}?page=1&{params}")
    return render_template("houses.html", houses=h, prev=prev)


@app.route("/books", methods=["GET"])
def books():
    params =''
    prev=False
    if request.query_string:
        params = request.query_string.decode()
        prev=True
    b = books_query(f"{BOOKS_ENDPOINT}?page=1&{params}")
    return render_template("books.html", books=b, prev=prev)

@app.route("/details/<id_>", methods=["GET"])
def details(id_):
    character_detail = api_data(f"{CHARACTERS_ENDPOINT}{id_}")
    return render_template("single.html", details=character_detail, id=id_)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('error_handlers/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error_handlers/500.html'), 500