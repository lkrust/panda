from behave import *
import helpers.ui as ui


@given('I am using the greatest factorial calculator')
def step_impl(context):
    ui.navigate(context)


@given('I enter {number} on the field')
def enter_number(context, number):
    ui.get_number_field(context, number)


@when('I click Calculate! button')
def calculate(context):
    ui.calculate_button(context)


@then('I see \'The factorial of {number} is: {result}\'')
def result(context, number, result):
    ui.get_result_text(context, number, result)


@given('I click on {page}')
def step_impl(context, page):
    ui.click_on_link(context, page)
    
@then('I should see \'{expected_text}\'')
def result(context, expected_text):
    actual_text = ui.get_body_text(context)
    print(expected_text)
    print(actual_text)
    assert expected_text == actual_text
