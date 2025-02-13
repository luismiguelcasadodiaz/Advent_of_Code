# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import hashlib

puzzle_input = 'ckczppom'
secret_key ='abcdef'
positive_number= 1

while True:
    str2hash=puzzle_input + str(positive_number)
    md5 = hashlib.md5(str2hash.encode()).hexdigest()
    if md5[0:6] =='000000': break
    positive_number +=1
print(positive_number)