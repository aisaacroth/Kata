#!/usr/bin/env python3.4
''' Test for the josephus program.

Author: Alexander Roth
Date:   2015-05-25
'''
from josephus import josephus
import unittest

class TestJosephus(unittest.TestCase):

    def setUp(self):
        self.test_case_1 = [1, 2, 3, 4, 5, 6, 7]
        self.test_case_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.test_case_3 = ['C', 'o', 'd', 'e', 'W', 'a', 'r', 's']

        self.test_answer_1 = [3, 6, 2, 7, 5, 1, 4]
        self.test_answer_2 = [2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
        self.test_answer_3 = ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']

    def test_first_case(self):
        tmp_list = josephus(self.test_case_1, 3)
        self.assertEqual(tmp_list, self.test_answer_1)

    def test_second_case(self):
        tmp_list = josephus(self.test_case_2, 2)
        self.assertEqual(tmp_list, self.test_answer_2)

    def test_third_case(self):
        tmp_list = josephus(self.test_case_3, 4)
        self.assertEqual(tmp_list, self.test_answer_3)

    def test_fourth_case(self):
        tmp_list = josephus(self.test_case_2, 1)
        self.assertEqual(tmp_list, self.test_case_2)

    def test_fifth_case(self):
        tmp_list = josephus([], 3)
        self.assertEqual(tmp_list, [])


if __name__ == '__main__':
    unittest.main()
