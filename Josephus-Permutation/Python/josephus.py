#!/usr/bin/env python3.4
'''
Module for the josephus permutation.

Author: Alexander Roth
Date:   2015-05-25
'''

def josephus(items, k):
    ''' 
    Returns the josephus permutation of the given list, generated from the
    specified k value.
    '''
    if len(items) == 0:
        return []

    if len(items) == 1:
        return [items[0]]

    i = ((k - 1) % len(items))
    return [items[i]] + josephus(items[i + 1:] + items[:i], k)
