from Pages.login_page import LoginPage
from Objects.account import Account
from TestCases.base_test import BaseTest
from TestData.TestData import TestData
from Pages.product_page import ProductPage
from TestCases.test_login import Login

class ProductPage(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_product_visible(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME, TestData.PASSWORD)
    login_page.login(account)

    expected_product_name = 'Sauce Labs Backpack'
    current_product_name = ProductPage.get_product_name
    self.assertEqual(expected_product_name, current_product_name, 'It does not exist.')