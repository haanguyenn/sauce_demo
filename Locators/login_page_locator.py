from selenium.webdriver.common.by import By

class LoginPageLocators(object):
  INPUT_USERNAME = (By.XPATH, '//*[@id="user-name"]')
  INPUT_PASSWORD = (By.XPATH, '//*[@id="password"]')
  BTN_LOGIN = (By.XPATH, '//*[@id="login-button"]')
  LABEL_MESSAGE = (By.XPATH, '//*[@id="login_button_container"]/div/form/h3')
