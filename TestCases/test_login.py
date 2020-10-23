from Pages.login_page import LoginPage
from Objects.account import Account
from TestCases.base_test import BaseTest
from TestData.TestData import TestData
import time

class Login(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_login_standard(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.USERNAME, TestData.PASSWORD)
    login_page.login(account)

    current_url = login_page.get_current_url()
    expected_url = 'https://www.saucedemo.com/inventory.html'
    #print(current_url)
    self.assertEqual(expected_url, current_url, 'The current URL does not match with the expected URL.')

  def test_login_locked_out(self):
    login_page = LoginPage(self.driver)
    account = Account('locked_out_user', TestData.PASSWORD)
    login_page.login(account)
    error_message = 'Epic sadface: Sorry, this user has been locked out.'
    time.sleep(5)
    # print(login_page.get_message())
    self.assertIn(error_message, login_page.get_message())

  def test_login_problem(self):
    login_page = LoginPage(self.driver)
    account = Account('problem_user', TestData.PASSWORD)
    login_page.login(account)

    current_url = login_page.get_current_url()
    expected_url = 'https://www.saucedemo.com/inventory.html'
    self.assertEqual(expected_url, current_url, 'The current URL does not match with the expected URL.')

  def test_login_performance_glitch(self):
    login_page = LoginPage(self.driver)
    account = Account('performance_glitch', TestData.PASSWORD)
    login_page.login(account)

    current_url = login_page.get_current_url()
    expected_url = 'https://www.saucedemo.com/inventory.html'
    self.assertEqual(expected_url, current_url, 'The current URL does not match with the expected URL.')
