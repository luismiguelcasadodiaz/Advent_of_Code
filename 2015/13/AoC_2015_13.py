# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:23:10 2023

@author: luism
"""
"""
In years past, the holiday feast with your family hasn't gone so well. 
Not everyone gets along! This year, you resolve, will be different. 
You're going to find the optimal seating arrangement and avoid all those 
awkward conversations.

You start by writing up a list of everyone invited and the amount their 
happiness would increase or decrease if they were to find themselves sitting 
next to each other person. You have a circular table that will be just big 
enough to fit everyone comfortably, and so each person will have exactly 
two neighbors.

For example, suppose you have only four attendees planned, and you calculate 
their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units 
(because David talks so much), but David would gain 46 happiness units 
(because Alice is a good listener),
 for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice 
(Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob 
(Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). 
The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, 
you find that this one is the most optimal, with a total change in happiness 
of 330.

What is the total change in happiness for the optimal seating arrangement of 
the actual guest list?

"""

def get_rules()->list:
  """
  Trasts the input file.
  the input fales has rules wiht this format:
  Alice would lose 2 happiness units by sitting next to Bob.
  that is splite into a rule/list like this
  'Alice','would','lose','2','happiness',....,'next','to','Bob.']
  
  where the relevante elemente are
  rule[0] Rule owner
  rule[-1][:-1] Applies when owner sits next to him/her (Last one witho point)
  rule[2] says if there is gain or lost of hapiness
  rule[3] hapiness change
  
  

  Returns
  -------
  list
    List of rules: each rule has two names and a value:
      [rule[0], rule[-1], value]
      The value is tha hapiness changes of the first when sitted next the other

  """
  my_rules=[]
  with open("input.txt",'r') as f:
    for line in f:
      rule=line.strip().split()
      if rule[2] == 'gain':
        value = int(rule[3])
      else:
        value = - int(rule[3])
      my_rules.append([rule[0], rule[-1][:-1], value])
  return my_rules


rules=get_rules()
print(len(rules))