# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:58:55 2023

@author: luism
"""

input="1321131112"
txt_in=list(input)
txt_out=[]
prev_char=txt_in[0]
count=0
for i in range(50):
  print(i,len(txt_in))
  for char in txt_in:
    if char != prev_char:
      txt_out.append(str(count))
      txt_out.append(prev_char)
      prev_char = char
      count = 1
    else:
      count +=1
  txt_out.append(str(count))
  txt_out.append(prev_char)
  txt_in = txt_out.copy()
  txt_out=[]
  prev_char=txt_in[0]
  count=0
print("part_one the lengh is {}".format(len(txt_in)))