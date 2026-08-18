from pages.home_page import HomePage

class TestFormPage:
    def test_open_practice_form(self,driver):
        form_page = HomePage(driver).open().open_forms()


