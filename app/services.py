import json
from typing import List, Union

import requests

PEOPLE_ENDPOINT = "/characters/"
GOT_ENDPOINT = "https://anapioficeandfire.com/api/"


def api_data(endpoint) -> str:
    res = requests.get(f"{GOT_ENDPOINT}{endpoint}")
    return res.json()


def get_list_data(list, key) -> List[Union[int, str, float]]:
    info = []
    for _ in range(len(list)):
        r = requests.get(list[_])
        info.append(r.json()[key])
    return info


def houses_query(endpoint) -> str:
    """Returns GOT Houses data
    Args:
        endpoint: Str
    Result:
        data: Dict
    """
    data = api_data(endpoint)
    for _ in range(len(data)):
        swornMembers = get_list_data(data[_]["swornMembers"], "name")
        if not data[_]["name"]:
            data[_]["name"] = "No name"
        data[_]["swornMembers"] = swornMembers
    return data


def characters_query(endpoint) -> str:
    """Returns GOT Characters data
    Args:
        endpoint: Str
    Result:
        data: Dict
    """
    data = api_data(endpoint)
    for _ in range(len(data)):
        books = get_list_data(data[_]["books"], "name")
        if not data[_]["name"]:
            data[_]["name"] = "No name"
        data[_]["books"] = books
    return data
