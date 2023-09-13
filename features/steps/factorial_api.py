from behave import *
import requests



@given('I want to know the factorial of {number}')
def step_impl(context, number):
    context.number = number

@when('I make the request')
def step_impl(context):

    url = "https://pandaqaetest.pythonanywhere.com/factorial"

    payload = f'number={context.number}'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': '*/*',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://pandaqaetest.pythonanywhere.com',
    'Connection': 'keep-alive',
    'Referer': 'https://pandaqaetest.pythonanywhere.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    context.result = response.json().get('answer')


@then('I see the result is {result}')
def step_impl(context, result):

    assert context.result == int(result)
