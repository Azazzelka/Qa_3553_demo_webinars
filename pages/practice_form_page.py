import platform
from time import sleep

from selenium.webdriver.common.by import By

from models.enums import Gender, Hobbies
from models.student import Student
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class PracticeFormPage(BasePage):
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    EMAIL = (By.CSS_SELECTOR, "#userEmail")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.XPATH, "//input[@id='dateOfBirthInput' "
                               "or @class='form-control react-datepicker-ignore-onclickoutside']")
    SUBJECTS = (By.CSS_SELECTOR, "input#subjectsInput.subjects-auto-complete__input")
    CURR_ADDRESS = (By.XPATH, "//textarea[@placeholder='Current Address']")
    STATE = (By.ID, "react-select-3-input")
    CITY = (By.ID, "react-select-4-input")
    BTN_SUBMIT = (By.XPATH, "//button[text()='Submit']")

    def fill_and_click_submit(self, student: Student) -> None:
        self.fill(self.FIRST_NAME, student.first_name)
        self.fill(self.LAST_NAME, student.last_name)
        self.fill(self.EMAIL, student.email)
        self._choose_gender(student.gender)
        self.fill(self.MOBILE, student.mobile)
        self._set_date_of_birth(student.date_of_birth)
        self._add_subjects(student.subject)
        self._choose_hobbies(student.hobbies)



    def _choose_gender(self, gender : Gender):
         self.click((By.ID, gender.locator))


    def _set_date_of_birth(self, date_of_birth: str) -> None:
        field_date = self.visibility(self.DATE_OF_BIRTH)
        field_date.click()
        select_all = Keys.COMMAND if platform.system() == "Darwin" else Keys.CONTROL
        field_date.send_keys(select_all, "a")
        field_date.send_keys(date_of_birth, Keys.ENTER)

    def _add_subjects(self, subjects: str) -> None:
        field_sub = self.visibility(self.SUBJECTS)
        field_sub.click()
        for subject in subjects.split(","):
            field_sub.send_keys(subject)
            field_sub.send_keys(Keys.ENTER)

    def _choose_hobbies(self, hobbies: list[Hobbies]) -> None:
        for hobby in hobbies:
            locator = (
                By.CSS_SELECTOR,
                f"label[for='{hobby.locator}']"
            )
            self.click(locator)
