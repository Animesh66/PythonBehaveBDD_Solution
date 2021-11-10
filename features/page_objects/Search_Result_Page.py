from features.page_objects.Base_Page import BasePage

class SearchResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_result(self):
        all_links = self.search_links("search_links_XPATH")
        self.click_element(all_links[0])





