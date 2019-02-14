import json


def parse_json_username_github_data(json_data):
    temp = json.dumps(json_data)
    data = json.loads(temp)
    return [data['items'][0]['login'], data['items'][0]['repos_url']]


def parse_json_repositories_list(json_data):
    data = json.loads(json.dumps(json_data))
    return list(map(lambda x: x['name'], data))
