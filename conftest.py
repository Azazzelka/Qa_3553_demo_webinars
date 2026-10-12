import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from models.enums import Gender, Hobbies
from models.student import Student
from faker import Faker

fake = Faker()


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def student() -> Student:
    return Student(
        first_name=fake.unique.first_name(),
        last_name=fake.unique.last_name(),
        email=fake.unique.email(),
        gender= Gender.FEMALE,
        mobile=fake.numerify("##########"),
        date_of_birth="22 Nov 1999",
        subject="Math,English,History",
        hobbies=[Hobbies.SPORT, Hobbies.READING, Hobbies.MUSIC],
        picture="",
        curr_address="Street 1 app. 67",
        state="NCR",
        city="Delhi",
    )