#!/usr/bin/env python3.4
''' Tester for the delete_nth element program

Author: Alexander Roth
Date:   2015-05-25
'''
from delete_nth import delete_nth
import unittest

class TestDeleteNth(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_list_of_2(self):
        test_list = delete_nth([1, 1, 1, 1], 2)
        self.assertEqual(test_list, [1, 1])

    def test_list_of_1(self):
        test_list = delete_nth([20, 37, 20, 21], 1)
        self.assertEqual(test_list, [20, 37, 21])

if __name__ == '__main__':
    unittest.main()
