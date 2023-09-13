import requests

BASE_URL = 'https://pandaqaetest.pythonanywhere.com'

def post(number):
    url = f'{BASE_URL}/factorial'

    payload = f'number={number}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    return requests.request("POST", url, headers=headers, data=payload)
