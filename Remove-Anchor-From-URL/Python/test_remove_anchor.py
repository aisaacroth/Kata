'''

Author: Alexander Roth
Date:   2015-01-05
'''
from remove_anchor import remove_url_anchor
import unittest

class TestRemoveAnchor(unittest.TestCase):

    def setUp(self):
        pass

    
    def test_with_anchor(self):
        test_url = remove_url_anchor('www.codewars.com#about')
        self.assertEqual(test_url, 'www.codewars.com')


    def test_without_anchor(self):
        test_url = remove_url_anchor('www.codewars.com?page=1')
        self.assertEqual(test_url, 'www.codewars.com?page=1')


if __name__ == '__main__':
    unittest.main()

