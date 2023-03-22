# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 12:09:31 2023

@author: luism
"""
"""
The elves bought too much eggnog again - 150 liters this time. 
To fit it all into your refrigerator, you'll need to move it into smaller 
containers. 

You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. 

If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5

Filling all containers entirely, how many different combinations of containers 

can exactly fit all 150 liters of eggnog?
"""

"""
This is a problem of sum of sets:
  Several algoritms on internet explain how to answers yes/no to the question
  if there are a set of containers that contain excactly 150 liters.
  
  
  
"""
import os
def getdata(filename)->list:
  data=[]
  path = os.path.join(os.getcwd(), filename)
  with open(path,"r") as f:
    for line in f:
      data.append(int(line.strip()))
  return data


  
if __name__ == "__main__":
  settest=[20,15,10,5,5]
  sumtest=25
  
  setone=getdata("input.txt")
  sumone=150