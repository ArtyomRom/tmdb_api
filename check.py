import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('API_KEY')

proxies = {
    'http': 'http://216.229.112.25:8080',
    'https': 'http://216.229.112.25:8080'
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
method = '/movie/2'
params = {
    'api_key': api_key,
}
url = 'https://api.themoviedb.org/3%s' % method
response = requests.get(url, params=params, headers=headers, proxies=proxies)
# response = requests.get(url, headers=headers, proxies=proxies, params=params)
# response = requests.get(url, headers=headers, proxies=proxies)

# print(response.status_code)
print(response.text)
# print(response.json())
