from selenium.webdriver.common.by import By

class ProductPageLocators(object):
  BTN_ADD_TO_CART = (By. XPATH, '//*[@id="inventory_container"]/div/div[1]/div[3]/button')
  BTN_REMOVE_CART = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[3]/button')
  PRD_NAME = (By.XPATH, '//*[@id="item_4_title_link"]/div')