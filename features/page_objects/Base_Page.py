from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from BehaveBDDWithPageObjects.Utilities import configReader
import logging
from BehaveBDDWithPageObjects.Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).click()
        log.logger.info("Clicking on an element: " + str(locator))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element_by_xpath(configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element_by_id(configReader.readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element_by_id(configReader.readConfig("locators", locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)
        log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(value))

    def move_to(self, locator):

        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element_by_xpath(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element_by_css_selector(configReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element_by_id(configReader.readConfig("locators", locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        log.logger.info("Moving to an element: " + str(locator))
