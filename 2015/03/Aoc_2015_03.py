# -*- coding: utf-8 -*-
"""
SThe next year, to speed up the process, Santa creates a robot version of himself, 
Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location 
(delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
pyder Editor

This is a temporary script file.
"""


    
mykeys='^v<>' #this string code movement simbols
steps=[(0,1),(0,-1),(-1,0),(1,0)]

gifted_houses=dict()
gifted_houses[(0,0)]=1

coordinates=[[0,0],[0,0]]

with open('input.txt','r') as f:
    orders=f.readlines()
orders_count=0    
for order in orders[0]:
    step=steps[mykeys.index(order)]
    flag = (orders_count % 2 != 0)
    coordinates[flag][0]+= step[0]
    coordinates[flag][1]+= step[1]
    gifted_houses.setdefault((coordinates[flag][0],coordinates[flag][1]),1)
    orders_count +=1
    print('{} order {} x={}, y={}. Houses = {}'.format(flag, 
                                                       order, 
                                                       coordinates[flag][0],
                                                       coordinates[flag][1],
                                                       len(gifted_houses)))
print(len(gifted_houses) )