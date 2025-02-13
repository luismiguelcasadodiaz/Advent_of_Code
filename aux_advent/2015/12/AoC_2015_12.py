# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:17:16 2023

@author: luism
"""
"""
--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent order. 
Unfortunately, their accounting software uses a peculiar storage format. 
That's where you come in.

They have a JSON document which contains a variety of things: 
  arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. 
  Your first job is to simply find all of the numbers throughout the document 
  and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

"""
import json

def santa_sum(account)->int:
  """
  Recursively summs the integer values of the JSON document
  if the document's element is a list accumulates each list elemnt
  if the document's element is a dict accumulates each dict value
  if the document's element is a str return 0
  if the document's element is a int returns the value
  

  Parameters
  ----------
  account : TYPE
    JSON document

  Returns
  -------
  int
    sum of integer values

  """
  my_sum=0
  my_type = type(account)
  if my_type == list:
    for elem in account:
      my_sum += santa_sum(elem)
    return my_sum
  elif my_type == dict:
    for elem in account.values():
      my_sum += santa_sum(elem)
    return my_sum
  elif my_type == str:
    return  0
  elif my_type == int:
    return account
  else:
    print(my_type)
    return account
  
def santa_sum2(account)->int:
  """
  Recursively summs the integer values of the JSON document
  if the document's element is a list accumulates each list elemnt
  if the document's element is a dict accumulates each dict value
  if the document's element is a str return 0
  if the document's element is a int returns the value
  

  Parameters
  ----------
  account : TYPE
    JSON document

  Returns
  -------
  int
    sum of integer values

  """
  my_sum=0
  my_type = type(account)
  if my_type == list:
    for elem in account:
      my_sum += santa_sum2(elem)
    return my_sum
  elif my_type == dict:
    if "red" not in account.values():
      for elem in account.values():
        my_sum += santa_sum2(elem)
      return my_sum
    else:

      return 0
  elif my_type == str:
    return  0
  elif my_type == int:
    return account
  else:
    print(my_type)
    return account
    

  
tests=[[1,2,3],
       {'a':2,'b':4},
       [[[3]]],
       {"a":{"b":4},"c":-1},
       {"a":[-1,1]},
       [-1,{"a":1}],
       [],
       {},
       [1,{"c":"red","b":2},3],
       {"d":"red","e":[1,2,3,4],"f":5},
       [1,"red",5]]
for test in tests:
  print("Test: sum of {} is {}".format(test,santa_sum2(test)))
  print("----------------------")
       

f=open('input.txt','r')
account=json.load(f)
f.close()

print("Part one: sum of JSON document is {}".format(santa_sum(account)))
print("Part two: sum of JSON document is {}".format(santa_sum2(account)))
