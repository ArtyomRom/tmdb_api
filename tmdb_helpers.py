import json
import urllib.parse
import urllib.request
from getpass import getpass
import urllib.request
import urllib.error
import os
from dotenv import load_dotenv
def make_tmdb_api_request(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params, headers)


def load_json_data_from_url(base_url, url_params, headers=None):
    url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
    # url_with_headers = urllib.request.Request(url, headers=headers or {})
    # response = urllib.request.urlopen(url).read().decode('utf-8')
    proxies = {
        'http': 'http://216.229.112.25:8080',
        'https': 'http://216.229.112.25:8080'
    }
    proxy = urllib.request.ProxyHandler(proxies)

    # Создаем объекты с помощью прокси
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    request = urllib.request.Request(url, headers=headers or {}) # Создаем объект Request
    response = urllib.request.urlopen(request).read().decode("utf-8")
    return json.loads(response)
    # return json.loads(data)


def get_user_api_key():
    load_dotenv()
    api_key = os.environ.get('API_KEY')
    # user_api_key = getpass('Enter your api key v3:')
    user_api_key = api_key
    try:
        make_tmdb_api_request(method='/movie/2', api_key=user_api_key)
        return user_api_key

    except urllib.error.URLError as err:
        if isinstance(err.reason, OSError) and err.reason.errno in (10054, 10060):
            return api_key
    except urllib.error.HTTPError as err:
        if err.code == 401:
            return None
        else:
            raise
