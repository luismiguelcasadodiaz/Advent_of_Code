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
--- Part Two ---
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old
scoring system.

Instead, at the end of each second, he awards one point to the reindeer 
currently in the lead. 

(If there are multiple reindeer tied for the lead, they each get one point.) 

He keeps the traditional 2503 second time limit, of course, as doing otherwise 
would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the
lead and gets one point. He stays in the lead until several seconds into 
Comet's second burst: after the 140th second, Comet pulls into the lead and 
gets his first point. Of course, since Dancer had been in the lead for the 139 
seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, 
our old champion, only has 312. So, with the new scoring system, 
Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after 
exactly 2503 seconds, how many points does the winning reindeer have?
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
  TRAVELED = 8
  POINTS = 9

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
      my_data.append([l[0],int(l[3]),int(l[6]),int(l[13]),0,0,0,0,0,0])
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
    r[idx.CYCLETIME.value]=r[idx.RUNTIME.value] + r[idx.WAITTIME.value]
    #How many cucles fit in simultaion time?
    r[idx.CYCLES.value]= simulation_length // r[idx.CYCLETIME.value]
    #calculate remainder time
    r[idx.REMAINDER.value]= simulation_length % r[idx.CYCLETIME.value]
    #distance traveled in one cycle
    distance = r[idx.SPEED.value] *  r[idx.RUNTIME.value]
    
    if r[idx.REMAINDER.value] >= r[idx.RUNTIME.value]:
      #remainder is enoug for one more run time. Equals one moer cycle.
      distance *= (r[idx.CYCLES.value]+1) 
      r[idx.DISTANCE.value]=distance
    else:
      #remainder is not enough for one more cycle
      distance *= r[idx.CYCLES.value] # times number of cycles
      #plus remainder time at speed
      distance += r[idx.SPEED.value] * r[idx.REMAINDER.value]
      r[idx.DISTANCE.value]=distance 
  return sorted(data, key = lambda x:x[idx.DISTANCE.value], reverse=True)
    
def calculate_points(data):
  for t in range(1,simulation_length+1):

    for r in data:
      #How many cucles fit in simultaion time?
      r[idx.CYCLES.value] = t // r[idx.CYCLETIME.value]
      #calculate remainder time
      r[idx.REMAINDER.value] = t % r[idx.CYCLETIME.value]
      #calculate distance traveled in previous cycles
      distance = r[idx.SPEED.value] * r[idx.RUNTIME.value]* r[idx.CYCLES.value]
      #checking sotiation at actual cycle
      if r[idx.REMAINDER.value] <= r[idx.RUNTIME.value]:
        distance += r[idx.REMAINDER.value] * r[idx.SPEED.value]
      else:
        distance += r[idx.RUNTIME.value] * r[idx.SPEED.value]
      r[idx.TRAVELED.value] = distance
    #sort by traveled distance
    data.sort(key=lambda x: x[idx.TRAVELED.value], reverse=True)
    #add a point to the winner
    data[0][idx.POINTS.value]  +=1
    #check if other are tied
    for r in data[1:]:
      if r[idx.TRAVELED.value] == data[0][idx.TRAVELED.value]:
        r[idx.POINTS.value] +=1
      else:
        break #data is ordere, in not mach sucessor neither match
        
  #sort by points
  data.sort(key=lambda x: x[idx.POINTS.value], reverse=True)
  

#test data      
simulation_length=1000
data=get_data("test.txt")
sorted_data = pre_process(data)
calculate_points(sorted_data)
print("Wiht test data {} wins with {} points".format(
  sorted_data[0][idx.NAME.value],  
  sorted_data[0][idx.POINTS.value]))

#input data
simulation_length=2503
data=get_data("input.txt")
sorted_data = pre_process(data)
calculate_points(sorted_data)
print("Wiht input data {} wins with {} points".format(
  sorted_data[0][idx.NAME.value],  
  sorted_data[0][idx.POINTS.value]))
