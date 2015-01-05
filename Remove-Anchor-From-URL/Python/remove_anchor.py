#!/usr/bin/env python3
'''

Author: Alexander Roth
Date:   2015-01-05
'''

def remove_url_anchor(url):
    return url[:url.index('#')] if '#' in url else url

