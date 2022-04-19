from unittest import TestLoader, TestSuite, TextTestRunner
from tests.test_home_page import TestHomePage
from tests.test_login_page import TestLoginPage

import testtools as testtools

if __name__ == "__main__":

  test_loader = TestLoader()
  # Test Suite is used since there are multiple test cases
  test_suite = TestSuite((
      # test_loader.loadTestsFromTestCase(TestLoginPage),
      test_loader.loadTestsFromTestCase(TestHomePage),
      ))

  test_runner = TextTestRunner(verbosity=2)
  test_runner.run(test_suite)
  # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
  parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
  parallel_suite.run(testtools.StreamResult())
