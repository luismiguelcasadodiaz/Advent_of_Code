# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:45:44 2023

@author: luism
"""
"""
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a 
thank you card. 

However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which
Aunt Sue (which you conveniently number 1..500, for sanity) gave you the gift. 
You open the present and, as luck would have it, good ol' Aunt Sue got you a 
My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the 
case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few 
specific compounds in a given sample, as well as how many distinct kinds of 
those compounds there are. According to the instructions, these are what the 
MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from 
the gift into the MFCSAM. It beeps inquisitively at you a few times and then 
prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue. 
Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?
"""

"""
First i check the input lines. All have 8 items
Also I check how many unique compunds are in the input lines
"""
import os
def get_data(filename):
  path=os.path.join(os.getcwd(), filename)
  compounds={}
  with open(path,"r") as f:
    for line in f:
      myline = line.strip().split(" ")
      #print(myline)
      line=[]
      for e in myline:
        e=e.strip(":")
        e=e.strip(",")
        e=e.strip(" ")
        try: 
          e=int(e)
          line.append(e)
        except:
          line.append(e)

      #if len(myline) != 8: print((myline))
      if (paper[line[2]] == line[3] and 
          paper[line[4]] == line[5] and 
          paper[line[6]] == line[7]):
          print(line)
        
"""      compounds.setdefault(myline[2],0)
      compounds.setdefault(myline[4],0)
      compounds.setdefault(myline[6],0)
  print(compounds)
"""
if __name__ == "__main__":
  
  paper=dict({"children": 3,  "cats": 7,  "samoyeds": 2,  "pomeranians": 3,
              "akitas": 0,  "vizslas": 0,  "goldfish": 5,  "trees": 3,
              "cars": 2,  "perfumes": 1})
  data=get_data(("input.txt"))