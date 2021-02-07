from typing import List, Union
from hashlib import md5
import requests


GOT_ENDPOINT = "https://anapioficeandfire.com/api"

def api_data(endpoint) -> str:
    resp = requests.get(f"{GOT_ENDPOINT}{endpoint}")
    return resp.json()

def get_list_data(list, key, is_list=True) -> List[Union[int, str, float]]:
    if is_list:
        info = []
        for _ in range(len(list)):
            r = requests.get(list[_])
            info.append(r.json()[key])
        return info
    elif not list:
        return 'no data'
    else:
        r = requests.get(list)
        return r.json()[key]


def houses_query(endpoint) -> str:
    """Returns GOT Houses data
    Args:
        endpoint: Str
    Result:
        data: Dict
    """
    data = api_data(endpoint)
    for _ in range(len(data)):
        data[_]["currentLord"] = get_list_data(data[_]["currentLord"], "name",is_list=False)
        data[_]["heir"] = get_list_data(data[_]["heir"], "name", is_list=False)
        data[_]["overlord"] = get_list_data(data[_]["overlord"], "name", is_list=False)
        if not data[_]["name"]:
            data[_]["name"] = "No name"
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


def books_query(endpoint) -> str:
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