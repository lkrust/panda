from behave import *
# from selenium import webdriver
import time


@given('I am using the greatest factorial calculator')
def step_impl(context):
    context.driver.get('https://pandaqaetest.pythonanywhere.com/')


@given('I enter {number} on the field')
def click_start_button(context, number):
    context.driver.find_element(by='id', value='number').send_keys(number)


@when('I click Calculate! button')
def select_yes_all_answers(context):
    context.driver.find_element(by='id', value='getFactorial').click()



@then('I see \'The factorial of {number} is: {result}\'')
def select_no_in_an_answer(context, number, result):
    context.driver.wait_until_text_present(2, 'resultDiv', f'The factorial of {number} is: {result}')

