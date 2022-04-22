from unittest import TestLoader, TestSuite, TextTestRunner
from tests import TestHomePage
from tests import TestLoginPage
from tests import TestSearchChatUser
from tests import TestAdminPage

import testtools as testtools

if __name__ == "__main__":

  test_loader = TestLoader()
  # Test Suite is used since there are multiple test cases
  test_suite = TestSuite((
    test_loader.loadTestsFromTestCase(TestLoginPage),
    test_loader.loadTestsFromTestCase(TestHomePage),
    test_loader.loadTestsFromTestCase(TestSearchChatUser),
    test_loader.loadTestsFromTestCase(TestAdminPage),
  ))

  test_runner = TextTestRunner(verbosity=2)
  test_runner.run(test_suite)
  # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
  parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
  parallel_suite.run(testtools.StreamResult())
