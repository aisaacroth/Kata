#!/usr/bin/env python3
''' Tester to test if power set function works.

Author: Alexander Roth
Date:   2015-01-06
'''
from count_power_sets import count_power_set
import unittest

class TestCountPSet(unittest.TestCase):

    def setUp(self):
        pass

    def testEmptySet(self):
        test_set = []
        p_num = count_power_set(test_set)
        self.assertEqual(p_num, 1)

    def testRealSet(self):
        test_set = [1, 2, 3]
        p_num = count_power_set(test_set)
        self.assertEqual(p_num, 8)

if __name__ == '__main__':
    unittest.main()
