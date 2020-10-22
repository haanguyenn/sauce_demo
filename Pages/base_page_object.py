from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasedPage():

  def __init__(self, driver):
    self.driver = driver
    self.timeout = 30

  def navigate_to(self, url):
    self.driver.get(url)

  def click(self, by_locator):
    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    element.click()

  def enter_text(self, by_locator, value):
    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    element.send_keys(value)

  def get_text(self, by_locator):
    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    return element.text

  def get_current_url(self):
    return self.driver.current_url

  def close_browser(self):
    self.driver.close()
