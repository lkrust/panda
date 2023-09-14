import selenium.webdriver.support.expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait 

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def before_tag(context, tag):
    if tag == 'ui':
        # context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        context.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager(driver_version="116").install()))

        # Wait until text is present in the element
        def wait_until_text(time, element, text):
            return WebDriverWait(context.driver, time).until(EC.text_to_be_present_in_element(('id', element), text))

        context.driver.wait_until_text_present = wait_until_text
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)

def after_tag(context, tag):
        if tag == 'ui':
            context.driver.quit()