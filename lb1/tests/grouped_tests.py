import unittest
from array_utils_tests import TestArrayUtils
from string_operations_test import TestStringOperations


def grouped_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestArrayUtils))
    suite.addTest(unittest.makeSuite(TestStringOperations))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(grouped_tests())
