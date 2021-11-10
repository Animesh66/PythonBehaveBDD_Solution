from features.page_objects.Base_Page import BasePage
from features.page_objects.Search_Result_Page import SearchResultPage


class GoogleSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_url(self, url):
        self.driver.get(url)

    def type_search_term(self, search_term):
        self.type("search_box_XPATH", search_term)

    def click_search_button(self):
        self.click("search_button_XPATH")

