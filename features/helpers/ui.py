from helpers.common import BASE_URL
from behave import *

NUMBER_INPUT = 'number'
CALCULATE_BUTTON = 'getFactorial'
RESULT_TEXT = 'resultDiv'

def navigate(context):
    context.driver.get(BASE_URL)

def get_number_field(context):
    return context.driver.find_element(by='id', value=NUMBER_INPUT)

def calculate_button(context):
    return context.driver.find_element(by='id', value=CALCULATE_BUTTON)

def get_result_text(context, number, result):
    return context.driver.wait_until_text_present(2, RESULT_TEXT, f'The factorial of {number} is: {result}')