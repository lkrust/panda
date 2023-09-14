from helpers.common import BASE_URL
from behave import *
import allure

NUMBER_INPUT = 'number'
CALCULATE_BUTTON = 'getFactorial'
RESULT_TEXT = 'resultDiv'

def navigate(context):
    context.driver.get(BASE_URL)
    file_name = 'landingpage'
    allure_attach(context, file_name)


def get_number_field(context, number):
    context.driver.find_element(by='id', value=NUMBER_INPUT).send_keys(number)
    file_name = 'number_input'
    allure_attach(context, file_name)



def calculate_button(context):
    context.driver.find_element(by='id', value=CALCULATE_BUTTON).click()
    file_name = 'calculate'
    allure_attach(context, file_name)


def get_result_text(context, number, result):
    context.driver.wait_until_text_present(2, RESULT_TEXT, f'The factorial of {number} is: {result}')
    file_name = 'result'
    allure_attach(context, file_name)


def allure_attach(context, file_name):
    path = f'%screenshots%/{file_name}.png'
    context.driver.save_screenshot(path)
    return allure.attach.file(
        path,
        name=f"{file_name}.png",
        attachment_type=allure.attachment_type.PNG
    )