import json
from functools import reduce


def parse_json_username_github_data(json_data):
    temp = json.dumps(json_data)
    data = json.loads(temp)
    return [data['items'][0]['login'], data['items'][0]['repos_url']]


def parse_json_repositories_list(json_data):
    data = json.loads(json.dumps(json_data))
    return [x['name'] for x in data]


def parse_litecoin_transactions(json_data):
    data = json.loads(json.dumps(json_data))
    float_list = [x['qty'] for x in data]
    r_value = reduce(lambda x, y: x + y, float_list)
    return r_value
