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
results in a total score of 62 842 880, which happens to be the best score 
possible given these ingredients. 

If any properties had produced a negative total, it would have instead become 
zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total 
score of the highest-scoring cookie you can make?

--- Part Two ---
Your cookie recipe becomes wildly popular! Someone asks if you can make another
recipe that has exactly 500 calories per cookie (so they can use it as a meal 
replacement). 

Keep the rest of your award-winning process the same (100 teaspoons, same 
ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 
40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 
100), 
The total calorie count would be 40*8 + 60*3 = 500. 
The total score would go down, though: only 57 600 000, 
the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total 
score of the highest-scoring cookie you can make with a calorie total of 500?

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

def calculate_blend2(teaspoons):
  """ As in part two i have to deal wiht Calories i adjust it
  """
  #create a dictionary for store operations.
  properties={}
  for k,v in ingredients[0][1].items():
      properties.setdefault(k,0)
      
  my_keys = list(properties.keys())
  for k in my_keys:
    for i,v in enumerate(ingredients):
      #here calculate a capacity of 44*-1 + 56*2 = 68
      properties[k] += teaspoons[i] * v[1][k]
      # check if negative
    if properties[k] <= 0:
      properties[k] = 0
      
  #Multiplying these together (68 * 80 * 152 * 76)
  multiplication = 1
  for k in my_keys[:-1]: #but Calories
    multiplication *= properties[k]
    
  return multiplication, properties["calories"]


if __name__ == "__main__":
  
  ingredients, numingredients, properties =get_data("test.txt")
  print(ingredients, numingredients, properties)
  
  teaspoons=[44,56]
  score, calories =calculate_blend2(teaspoons)
  txt="TEST:highest-scoring is {} made of this blend {}"
  print(txt.format(score, teaspoons))
  print("="*80)
  teaspoons=[40,60]
  score,calories= calculate_blend2(teaspoons)
  txt="TEST 2:highest-scoring is {} made of this blend {} with {} Calories"
  print(txt.format(score, teaspoons,calories))
  print("="*80)  
  
  
  ingredients, numingredients, properties=get_data("input.txt")
  print(ingredients, numingredients, properties)

  resultados=[]
  MaxScore=0
  Maxteaspoons=[]
  for s in range(100,0,-1):
    for p in range (100-s,0,-1):
      for f in range (100-s-p,0,-1):
        for a in range(100 -s-p-f,0,-1):
          if s + p + f + a == 100:
            teaspoons=[s,p,f,a]
            score, calories =calculate_blend2(teaspoons)
            resultados.append((calories,score))
            if score > MaxScore:
              MaxScore = score
              Maxteaspoons =teaspoons
  txt="ONE:highest-scoring is {} made of this blend {}"            
  print(txt.format(MaxScore, Maxteaspoons))
  print("="*80)
  calories500 = [x for x in resultados if x[0] == 500 and x[1] != 0]
  calories500.sort(key=lambda x:x[1], reverse=True)
  txt="TWO:with {} calories the highest-scoring is {}"            
  print(txt.format(calories500[0][0], calories500[0][1]))
  print("="*80)