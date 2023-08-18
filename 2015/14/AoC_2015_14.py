# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:58:49 2023

@author: luism
"""
"""
This year is the Reindeer Olympics! 

Reindeer can fly at high speeds, but must rest occasionally to recover their 
energy. 

Santa want to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting 
(not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. 

After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. 

On the 11th second, Comet begins resting (staying at 140 km), 
and Dancer continues on for a total distance of 176 km. 

On the 12th second, both reindeer are resting. 

They continue to rest until the 138th second, when Comet flies for another ten
 seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet 
is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). 

So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), 

after exactly 2503 seconds, what distance has the winning reindeer traveled?
"""
from enum import Enum
class idx(Enum):
  NAME = 0
  SPEED = 1
  RUNTIME = 2
  WAITTIME = 3
  CYCLETIME = 4
  CYCLES = 5
  REMAINDER = 6
  DISTANCE = 7

def get_data(filename:str)->list:
  """
  

  Parameters
  ----------
  filename : Str
    file name wiht data.

  Returns
  -------
  list
    list of tuples wiht this template
    ('Comet', '3', '37', '76')
    (reindeer, Speed, runtime, waittime)

  """
  my_data=[]
  with open(filename,"r") as f:
    for line in f:
      l = line.strip().split(" ")
      my_data.append([l[0],int(l[3]),int(l[6]),int(l[13])])
  return my_data
      
def pre_process(data)->list:
  """
  This funcion calculates traveled distance during simulation time:
  
    Each reinder cycles betwwen run and wait.
    I calculate how many cicles fit into simultation time
    DIstance = runtime * speed * num of clycles
    
    I take care at remainder time.
    If in te remainder time fits a run time then a cycle is added
    if not compute the distance ate the speed during remainder time.

  Parameters
  ----------
  data : list of list
  

  Returns
  -------
  list of list: Ordered reversed by distance traveled.

  """
  for  r in data:
    #Calculate cycle time
    r.append(r[idx.RUNTIME.value] + r[idx.WAITTIME.value])
    #How many cucles fit in simultaion time?
    r.append( simulation_length // r[idx.CYCLETIME.value])
    #calculate remainder time
    r.append( simulation_length % r[idx.CYCLETIME.value])
    #distance traveled in one cycle
    distance = r[idx.SPEED.value] *  r[idx.RUNTIME.value]
    
    if r[idx.REMAINDER.value] >= r[idx.RUNTIME.value]:
      #remainder is enoug for one more run time. Equals one moer cycle.
      distance *= (r[idx.CYCLES.value]+1) 
      r.append(distance)
    else:
      #remainder is not enough for one more cycle
      distance *= r[idx.CYCLES.value] # times number of cycles
      #plus remainder time at speed
      distance += r[idx.SPEED.value] * r[idx.REMAINDER.value]
      r.append(distance )
  return sorted(data, key = lambda x:x[idx.DISTANCE.value], reverse=True)
    
    

      
simulation_length=1000
data=get_data("test.txt")
sorted_data = pre_process(data)
print("Wiht test data {} wins and travels {}".format(
  sorted_data[0][idx.NAME.value],  
  sorted_data[0][idx.DISTANCE.value]))

simulation_length=2503
data=get_data("input.txt")
sorted_data = pre_process(data)
print("Wiht input data {} wins and travels {}".format(
  sorted_data[0][idx.NAME.value],  
  sorted_data[0][idx.DISTANCE.value]))