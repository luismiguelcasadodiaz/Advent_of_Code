#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:01:18 2023

@author: luis

Because your neighbors keep defeating you in the holiday house decorating 
contest year after year, you've decided to deploy one million lights in a 
1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed 
you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights 
at each corner are at 0,0, 0,999, 999,999, and 999,0. 

The instructions include whether to turn on, turn off, or toggle various 
INCLUSIVE ranges given as coordinate pairs. 

Each coordinate pair represents opposite corners of a rectangle, INCLUSIVE; 
a coordinate pair like 0,0 through 2,2 therefore  refers to 9 lights in a 
3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by
 doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, 
    turning off the ones that were on, and turning on the ones that were off.
    
    turn off 499,499 through 500,500 would turn off (or leave off) 
    the middle four lights.

After following the instructions, how many lights are lit?

here some instrucctions
turn off 363,899 through 948,935
turn on 271,845 through 454,882
turn off 376,528 through 779,640
toggle 767,98 through 854,853
toggle 107,322 through 378,688
turn off 235,899 through 818,932
turn on 445,611 through 532,705
toggle 629,387 through 814,577
toggle 112,414 through 387,421
toggle 319,184 through 382,203
turn on 627,796 through 973,940
toggle 602,45 through 763,151
turn off 441,375 through 974,545

"""



"""
                  01234567....
if line contains "turn on 445,611 through 532,705"    line[6] == 'n'
if line contains "turn off 235,899 through 818,932"   line[6] == 'f'
if line contains "toggle 629,387 through 814,577"     line[6] == ' '


def get_corners(line,action):
if line contains "turn on 271,845 through 454,882",line.split() returns 
['turn', 'on', '271,845', 'through', '454,882'], so corners are 2 and -1

if line contains "turn off 701,636 through 928,877", line.split() returns
['turn', 'off', '701,636', 'through', '928,877'], so corners are 2 and -1

if line contains "toggle 107,322 through 378,688'", line.split() returns
['toggle', '107,322', 'through', '378,688'], so corners are 1 and -1

          act=0,  act=1,  act= -1]
corners=[  0       1      -1  ]
corners=[[2,-1],[2,-1],[1,-1]]


"""
import numpy as np


def get_corners(line,action):
    global grid
    
    upper_left_corner = line[corners[action][0]]
    lower_right_corner = line[corners[action][1]]
    
    x0_str, y0_str = upper_left_corner.split(',')
    x1_str, y1_str = lower_right_corner.split(',')
    
    x0, y0, x1, y1 =int(x0_str), int(y0_str), int(x1_str), int(y1_str)
    if action == -1:
        grid[x0:x1+1, y0:y1+1] = -grid[x0:x1+1, y0:y1+1] +1
    else:
        grid[x0:x1+1, y0:y1+1] =action


                              
n=1000
grid = np.zeros((n,n))

corners=[[2,-1],[2,-1],[1,-1]]

action = 0 # -1, 0, 1
with open("input.txt",'r' ) as f:
    for line in f:
        if line[6] == 'n': action = 1    #light on
        if line[6] == 'f': action = 0    #light off'
        if line[6] == ' ': action = -1   #toggle -g +1
        get_corners(line.split(),action)
        
print(grid)
print(np.count_nonzero(grid))

"""
--- Part Two ---

You just finish implementing your winning light pattern when you realize you 
mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each 
light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of 
those lights by 1.

The phrase turn off actually means that you should decrease the brightness of 
those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of 
those lights by 2.

What is the total brightness of all lights combined after following Santa's 
instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""
import numpy as np


def get_corners(line,action):
    global grid
    
    upper_left_corner = line[corners[action][0]]
    lower_right_corner = line[corners[action][1]]
    
    x0_str, y0_str = upper_left_corner.split(',')
    x1_str, y1_str = lower_right_corner.split(',')
    
    x0, y0, x1, y1 =int(x0_str), int(y0_str), int(x1_str), int(y1_str)
    if action == -1:
        grid[x0:x1+1, y0:y1+1] +=2
    elif action == 0:
        g=grid[x0:x1+1, y0:y1+1]
        g=np.where(g>0, g-1, g)
        grid[x0:x1+1, y0:y1+1] = g
    else: #action == 1
        grid[x0:x1+1, y0:y1+1] +=1


                              
n=1000
grid = np.zeros((n,n))

corners=[[2,-1],[2,-1],[1,-1]]

action = 0 # -1, 0, 1
with open("input.txt",'r' ) as f:
    for line in f:
        if line[6] == 'n': action = 1    #light on
        if line[6] == 'f': action = 0    #light off'
        if line[6] == ' ': action = -1   #toggle abs(status + action)
        get_corners(line.split(),action)
        

print(np.sum(grid))