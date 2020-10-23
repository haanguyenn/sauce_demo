import unittest
from TestCases.test_login import Login

login = unittest.TestLoader().loadTestsFromTestCase(Login)
test_suite = unittest.TestSuite([login])
unittest.TextTestRunner().run(test_suite)
