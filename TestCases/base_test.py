from selenium import webdriver
import os
import unittest

class BaseTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()

  def tearDown(self):
    self.driver.close()
    self.driver.quit()
