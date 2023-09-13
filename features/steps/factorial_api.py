from behave import *
import helpers.api as api


@given('I want to know the factorial of {number}')
def step_impl(context, number):
    context.number = number

@when('I make the request')
def step_impl(context):

    response = api.post(context.number)
    assert response.status_code == 200
    context.result = response.json().get('answer')


@then('I see the result is {result}')
def step_impl(context, result):

    assert context.result == int(result)
