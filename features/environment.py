from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait 
import selenium.webdriver.support.expected_conditions as EC


def before_tag(context, tag):
    if tag == 'ui':
        context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Wait until text is present in the element
        def wait_until_text(time, element, text):
            return WebDriverWait(context.driver, time).until(EC.text_to_be_present_in_element(('id', element), text))


        context.driver.wait_until_text_present = wait_until_text
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)

def after_tag(context, tag):
        if tag == 'ui':
            context.driver.quit()