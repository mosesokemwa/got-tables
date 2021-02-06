import json
from typing import  AnyStr, List
import requests


PEOPLE_ENDPOINT = '/characters/'
GOT_ENDPOINT='https://anapioficeandfire.com/api/'

def api_data(endpoint) -> str:
    res = requests.get(f'{GOT_ENDPOINT}{endpoint}' )
    return res.json()

def get_list_data(list) -> List[AnyStr]:
    info = []
    for _ in range(len(list)):
        r = requests.get(list[_])
        info.append(r.json()['name'])
    return info


def characters(endpoint) -> str:
    data = api_data(endpoint)
    for _ in range(len(data)):
        books = get_list_data(data[_]['books'])
        if not data[_]['name']:
            data[_]['name'] = 'No name'
        data[_]['books'] = books
    return data