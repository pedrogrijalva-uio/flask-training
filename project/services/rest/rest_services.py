import requests
from requests import models

from .json_util import parse_json_username_github_data, parse_json_repositories_list


def request_site(url: str) -> models.Response:
    print(url)
    response = requests.get(url)
    return response


def get_github_username(email: str):
    url_github = 'https://api.github.com/'
    url_info_user = url_github + 'search/users?q=' + email.replace('@', '%40') + '+in:email'
    data = request_site(url_info_user).json()
    return parse_json_username_github_data(data)


def get_repos_by_user(url_repos: str):
    data_repos = request_site(url_repos).json()
    return parse_json_repositories_list(data_repos)
