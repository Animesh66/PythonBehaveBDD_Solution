from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.config_reader import config_reader
from features.page_objects.Google_Search_Page import GoogleSearchPage
from features.page_objects.Search_Result_Page import SearchResultPage


@given('I navigate to google.com')
def step_impl(context):
    context.search = GoogleSearchPage(context.driver)
    context.search.open_url(config_reader("basic configue", "test_url"))


@when('I typed "{search_term}" in the search box')
def step_impl(context, search_term):
    context.search.type_search_term(search_term)


@when('click on the search button')
def step_impl(context):
    context.driver.click_search_button()


@then('I click on the second visible link')
def step_impl(context):
    context.result = SearchResultPage(context.driver)
    context.result.click_result()


@then('verify that "{search_term}" is present on the page')
def step_impl(context, search_term):
    context.result.verify_search_term(search_term)
