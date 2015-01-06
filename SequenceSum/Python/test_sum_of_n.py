#!/usr/bin/env python3
''' Tester for sequence sum program.

Author: Alexander Roth
Date:   2015-01-06
'''
from sum_of_n import sum_of_n
import unittest

class TestSequenceSum(unittest.TestCase):

    def setUp(self):
        pass

    def testListSizeThree(self):
        self.assertEqual(sum_of_n(3), [0, 1, 3, 6])

    def testListSizeOne(self):
        self.assertEqual(sum_of_n(1), [0, 1])

    def testEmptyList(self):
        self.assertEqual(sum_of_n(0), [0])

    def testNegativeList(self):
        self.assertEqual(sum_of_n(-4), [0, -1, -3, -6, -10])

if __name__ == '__main__':
    unittest.main()
