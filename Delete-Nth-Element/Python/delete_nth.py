#! /usr/bin/env python3.4
'''
Removes the nth element of a list

Author: Alexander Roth
Date:   2015-05-25
'''

def delete_nth(order, max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e:
            ans.append(o)
    
    return ans
