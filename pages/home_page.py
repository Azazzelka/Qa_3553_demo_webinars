from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.forms_page import FormsPage


class HomePage(BasePage):
    URL = "https://demoqa.com/"
    FORMS_ITEM = (By.XPATH, '//div[@class="category-cards"]/a[2]')

    def open(self) -> 'HomePage':
        self.driver.get(self.URL)
        return self

    def open_forms(self) -> FormsPage:
        self.click(self.FORMS_ITEM)
        return FormsPage(self.driver)

