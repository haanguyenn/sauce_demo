class BasedPage():

  def __init__(self, driver):
    self.driver = driver

  def navigate_to(self, url):
    self.driver.get(url)

  def close_browser(self):
    self.driver.close()