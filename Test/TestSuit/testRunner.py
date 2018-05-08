from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.TestHomePage import TestHomePage
from Test.Scripts.TestMainPage import TestMainPage

import testtools as testtools

if __name__ == "__main__":

    loader = TestLoader()

    suite = TestSuite((
        loader.loadTestsFromTestCase(TestHomePage),
        loader.loadTestsFromTestCase(TestMainPage)
        ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    # concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    # concurrent_suite.run(testtools.StreamResult())
