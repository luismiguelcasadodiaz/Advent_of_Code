#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 01:33:39 2023

@author: luis

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or 
    aeiouaeiouaeiou.
    
    It contains at least one letter that appears twice in a row, like xx, 
    abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    
    It does not contain the strings ab, cd, pq, or xy, even if they are 
    part of one of the other requirements.

"""

import re
matcher1 = re.compile(r'[aeiou]')
matcher2 = re.compile(r'(.)\1+')
matcher3 = re.compile(r'ab|cd|pq|xy')
nice = 0
with open('input.txt','r') as f:
    for line in f:
        critery3 = len(matcher3.findall(line)) == 0
        if critery3:
            critery1 = len(matcher1.findall(line))>= 3
            critery2 = len(tuple(matcher2.finditer(line))) >= 1
            if critery1  and critery2:
                nice +=1
    print(nice, critery1, critery2, critery3, line, 
                          matcher1.findall(line),
                          tuple(matcher2.finditer(line)),
                          matcher3.findall(line))

print("Part 1 has {} nice lines".format(nice))

#part 2
"""
Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the 
    string without overlapping, like xyxy (xy) or aabcdefgaa (aa), 
    but not like aaa (aa, but it overlaps).
    
    It contains at least one letter which repeats with exactly one letter 
    between them, like xyx, abcdefeghi (efe), or even aaa.
"""
matcher1 = re.compile(r'(.{2}).*\1')
matcher2 = re.compile(r'(.).\1')
nice = 0
with open('input.txt','r') as f:
    for line in f:
        critery1 = len(matcher1.findall(line))>0
        critery2 = len(matcher2.findall(line))>0
        if critery1 and critery2:
            nice += 1
        print(nice, critery1, critery2, line, 
                      matcher1.findall(line),
                      matcher2.findall(line))
            

print("Part 2 has {} nice lines".format(nice))        