# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:20:30 2023

@author: luism
"""
"""
Today, you set out on the task of perfecting your milk-dunking cookie recipe. 
All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a 
list of the remaining ingredients you could use to finish the recipe 
(your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, 
and you have to be accurate so you can reproduce your results in the future.

The total score of a cookie can be found by adding up each of the properties 
(negative totals become 0) and then multiplying together everything except 
calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of 
cinnamon (because the amounts of each ingredient must add up to 100) would 
result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) 
results in a total score of 62842880, which happens to be the best score 
possible given these ingredients. 

If any properties had produced a negative total, it would have instead become 
zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total 
score of the highest-scoring cookie you can make?

"""
import os

def get_data(filename)->list:
  data=[]
  path=os.path.join(os.getcwd(), filename)
  with open(path,"r") as f:
    for line in f:
      l=line.strip().split(":")
      d=dict(x.strip().split(" ") for x in l[1].split(","))
      #convert dict str values into integer
      for k,v in d.items():
        d[k]=int(v)

      data.append([l[0],d])
      
  return data , len(data), len(data[0][1])

def calculate_blend(teaspoons):
  #create a dictionary for store operations. the dict ignores calories for now
  properties={}
  for k,v in ingredients[0][1].items():
    if k != "calories":
      properties.setdefault(k,0)
    
  for k in properties.keys():
    for i,v in enumerate(ingredients):
      #here calculate a capacity of 44*-1 + 56*2 = 68
      properties[k] += teaspoons[i] * v[1][k]
      # check if negative
    if properties[k] <= 0:
      properties[k] = 0
  #Multiplying these together (68 * 80 * 152 * 76)
  multiplication = 1
  for k in properties.keys():
    multiplication *= properties[k]
  return multiplication


if __name__ == "__main__":
  
  ingredients, numingredients, properties =get_data("test.txt")
  print(ingredients, numingredients, properties)
  
  teaspoons=[44,56]
  score=calculate_blend(teaspoons)
  print("TEST:highest-scoring is {} made of this blend {}".format(score, teaspoons))
  print("="*80)
  
  
  
  ingredients, numingredients, properties=get_data("input.txt")
  print(ingredients, numingredients, properties)

  
  MaxScore=0
  Maxteaspoons=[]
  for s in range(100,0,-1):
    for p in range (100-s,0,-1):
      for f in range (100-s-p,0,-1):
        for a in range(100 -s-p-f,0,-1):
          if s + p + f + a == 100:
            teaspoons=[s,p,f,a]
            score=calculate_blend(teaspoons)
            if score > MaxScore:
              Maxscore = score
              Maxteaspoons =teaspoons
              
  print("ONE:highest-scoring is {} made of this blend {}".format(Maxscore, Maxteaspoons))
  print("="*80)