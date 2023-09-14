import allure
import requests
from helpers.common import BASE_URL

def post(number, content_type=None):
    url = f'{BASE_URL}/factorial'

    payload = f'number={number}'
    headers = {
    'Content-Type': content_type or 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    
    allure_attach(response.status_code, response.text)

    return response

def get(endpoint):
    url = f'{BASE_URL}/{endpoint}'

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    response = requests.request("GET", url, headers=headers)

    allure_attach(response.status_code, response.text)

    return response

def get_privacy():
    return get('/privacy')


def get_terms():
    return get('/terms')

def allure_attach(status_code, response_txt):
    allure.attach(
        f'Request status code is {status_code}\nRequest text is: \n"{response_txt}"',
    )
