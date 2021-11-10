from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.config_reader import config_reader


@given('I navigate to google.com')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.google.com/")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()


@when('I typed "{search_term}" in the search box')
def step_impl(context, search_term):
    context.driver.find_element(By.XPATH, "//input[@title='Search']").send_keys(search_term)


@when('click on the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()


@then('I click on the second visible link')
def step_impl(context):
    context.search_links = context.driver.find_elements(By.XPATH, "//h3[@class='LC20lb DKV0Md']")
    context.link = context.search_links[0]
    context.link.click()


@then('verify that "{search_term}" is present on the page')
def step_impl(context, search_term):
    assert search_term in context.driver.page_source, "Given search text is present in the website."
    context.driver.quit()
