from selenium.webdriver.common.by import By

class CheckoutPageLocators(object):
  FIRSTNAME = (By.ID, 'first-name')
  LASTNAME = (By.ID, 'last-name')
  ZIPCODE = (By.ID, 'postal-code')
  BTN_CANCEL = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/a')
  BTN_CONTINUE = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/input')
  