from Pages.base_page_object import BasedPage
from Locators.login_page_locator import LoginPageLocators
from TestData.TestData import TestData


class LoginPage(BasedPage):
  def __init__(self, driver):
    super().__init__(driver)
    self.navigate_to(TestData.BASE_URL)

  def login(self, account):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
    self.click(LoginPageLocators.BTN_LOGIN)

  def get_message(self):
    return self.get_text(LoginPageLocators.LABEL_MESSAGE)
