from behave import *
import helpers.api as api


@given('I want to know the factorial of {number}')
def step_impl(context, number):
    context.number = number

@when('I make the request')
def step_impl(context):
    response = api.post(context.number)
    context.status_code = response.status_code
    context.result = response


@then('I see the result is {result}')
def step_impl(context, result):
    assert context.result.json().get('answer') == int(result)


@given('I want to know a bit about {topic}')
def step_impl(context, topic):
    pass


@when('I make a request to /privacy')
def step_impl(context):
    response = api.get_privacy()
    assert response.status_code == 200
    context.result = response.text


@then('I should get \'{response_text}\'')
def step_impl(context, response_text):
    assert context.result == response_text


@when('I make a request to /terms')
def step_impl(context):
    response = api.get_terms()
    assert response.status_code == 200
    context.result = response.text


@then('I get a {expected_status_code} status code')
def step_impl(context, expected_status_code):
    assert expected_status_code == context.status_code


@then('an error message \'{error_msg}\'')
def step_impl(context, error_msg):
    assert context.result == error_msg

@when(u'I use the wrong content-type')
def step_impl(context):
    response = api.post(context.number, 'The parrot is no more!')
    context.status_code = response.status_code
    context.result = response