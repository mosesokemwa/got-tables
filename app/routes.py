from os import environ
from flask import render_template, request, current_app as app
from .services import api_data, characters



CHARACTERS_ENDPOINT = '/characters/'

@app.route('/',  methods=['GET'])
def index():
    people = characters(f'{CHARACTERS_ENDPOINT}?page=1')
    return render_template('index.html', people=people)


@app.route('/details/<id_>', methods=['GET'])
def details(id_):
    character_detail = api_data(f'{CHARACTERS_ENDPOINT}{id_}')

    # new_details = {
    #     'name': details['name'],
    #     "height": details["height"],
    #     "mass": details["mass"],
    #     "hair_color": details["hair_color"],
    #     "skin_color": details["skin_color"],
    #     "eye_color": details["eye_color"],
    #     "birth_year": details["birth_year"]
    # }
    return render_template('single.html', details=character_detail, id=id_)
