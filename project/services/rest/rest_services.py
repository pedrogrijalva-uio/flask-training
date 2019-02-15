import requests
from requests import models

from .json_util import parse_json_username_github_data, parse_json_repositories_list, parse_litecoin_transactions


def request_site(url: str) -> models.Response:
    print(url)
    response = requests.get(url)
    return response


def get_litecoin_last_transactions():
    url = 'https://api.binance.com/api/v1/trades?symbol=LTCBTC'
    try:
        data = parse_litecoin_transactions(request_site(url).json())
    except Exception as ex:
        data = ''
    return data


def get_github_username(email: str):
    url_github = 'https://api.github.com/'
    url_info_user = url_github + 'search/users?q=' + email.replace('@', '%40') + '+in:email'
    try:
        data = parse_json_username_github_data(request_site(url_info_user).json())
    except Exception as ex:
        data = ''
    return data


def get_repos_by_user(url_repos: str):
    try:
        print(url_repos)
        data_repos = parse_json_repositories_list(request_site(url_repos).json())
    except Exception as ex:
        data_repos = []
    return data_repos
