from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

Locator = tuple[str,str]
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator:Locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator:Locator) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def visibility(self, locator: Locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def fill(self, locator: Locator, text):
        element = self.visibility(locator)
        element.clear()
        element.send_keys(text)

