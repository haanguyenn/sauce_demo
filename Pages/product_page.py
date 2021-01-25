from Pages.base_page_object import BasedPage
from Locators.product_page_locator import ProductPageLocators


class ProductPage(BasedPage):
  def __init__(self, driver):
    super().__init__(driver)

  def add_to_cart(self):
    self.click(ProductPageLocators.BTN_ADD_TO_CART)

  def remove_from_cart(self):
    self.click(ProductPageLocators.BTN_REMOVE_CART)

  def get_product_name(self):
    return self.get_text(ProductPageLocators.PRD_NAME)
