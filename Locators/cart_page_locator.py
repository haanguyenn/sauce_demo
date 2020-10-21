from selenium.webdriver.common.by import By

class CartPageLocators(object):
  BTN_REMOVE = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/button')
  BTN_CHECKOUT = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[2]')
  BTN_CONTINUE = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/a[1]')
