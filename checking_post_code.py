# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:31:53 2021

@author: Mojtaba
"""


'''Barresy dorosti kode posti'''
post_code = input('Please enter a post code: ')
if post_code.isnumeric() is True:
    if len(post_code) == 5:
        print('%s is a vallid post code' % post_code)
    else:
        print('%s is not a vallid post code' % post_code)
else:
    print('%s is not a vallid post code' % post_code)
