from features.page_objects.Base_Page import BasePage

class GoogleSearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_url(self, url):
        self.driver.get(url)

    def google_search(self, search_term):
        self.type("search_box_XPATH", search_term)
        self.click("search_button_XPATH")





