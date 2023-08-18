# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:02:32 2023

@author: luism
"""
floor = 0
pos = 0
with open("input.txt","r") as f:
  lines = f.readlines()

  for line in lines:
    for c in line:
      pos +=1
      if c == '(' : floor +=1
      if c == ')' : floor -=1
      if floor == -1 :
        print(pos)
        break