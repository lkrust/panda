import requests
from helpers.common import BASE_URL

def post(number):
    url = f'{BASE_URL}/factorial'

    payload = f'number={number}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    return requests.request("POST", url, headers=headers, data=payload)
