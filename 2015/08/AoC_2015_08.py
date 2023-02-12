# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 21:16:36 2023

@author: luism
"""
import re
single=re.compile(r'\\\\')
quote=re.compile(r'\\"')
hexa=re.compile(r'\\x[0-9a-f]{2}')
ctr=[]
num_char_str = 0
num_char_mem = 0
num_char_enc = 0
my_line=""
with open("input.txt",'r') as file:
  for line in file:
      my_line = line.strip().replace(" ","")[1:-1]
      l = len(my_line)
      x = [elem.start() for elem in single.finditer(my_line)]
      y = [elem.start() for elem in quote.finditer(my_line)]
      z = [elem.start() for elem in hexa.finditer(my_line)]
      num_char_str += l
      num_char_mem += l - 2 -len(x) - len(y) - 3*len(z) 
      print('"{}  ==> \ {}, " {}, x {}'.format(my_line, x, y, z))
  
print("part one {}".format(num_char_str - num_char_mem))
num_char_str = 0
num_char_mem = 0
num_char_enc = 0
my_line=""
with open("input.txt",'r') as file:
  for line in file:
      my_line = line.strip().replace(" ","")[1:-1]
      new_enc_line = line.strip().replace(" ","")
      l = len(my_line)
      x = [elem.start() for elem in single.finditer(my_line)]
      y = [elem.start() for elem in quote.finditer(my_line)]
      z = [elem.start() for elem in hexa.finditer(my_line)]
      num_char_str += l
      num_char_mem += l - 2 -len(x) - len(y) - 3*len(z) 
      print('"{}  ==> \ {}, " {}, x {}'.format(my_line, x, y, z))
      num_char_enc += l + 4 + len(x)*2 + len(y)*2 + len(z) 
  
print("part two {}".format(num_char_enc-num_char_str))
