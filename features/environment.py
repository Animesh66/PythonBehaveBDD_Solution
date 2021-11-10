from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.config_reader import config_reader
import allure


def before_scenario(context):
    if config_reader("basic configure", "browser") == "chrome":
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
    elif config_reader("basic configure", "browser") == "firefox":
        context.driver = webdriver.Firefox(GeckoDriverManager().install())
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)


def after_scenario(context):
    context.driver.quit()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
