# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:13:11 2023

@author: luism
"""

"""
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has 
devised a method of coming up with a password based on the previous one. 

Corporate policy dictates that passwords must be exactly eight lowercase 
letters (for security reasons), so he finds his new password by incrementing
his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on.

Increase the rightmost letter one step; 

if it was z, it wraps around to a, and repeat with the next letter to the left 
until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has 
imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, 
like abc, bcd, cde, and so on, up to xyz. 

They cannot skip letters; abd doesn't count.

Passwords may not contain the letters i, o, or l, as these letters can be 
mistaken for other characters and are therefore confusing.

Passwords must contain at least two different, non-overlapping pairs of 
letters, like aa, bb, or zz.

For example:

hijklmmn meets the first requirement (because it contains the straight hij) 
but fails the second requirement requirement (because it contains i and l).

abbceffg meets the third requirement (because it repeats bb and ff) 
but fails the first requirement.

abbcegjk fails the third requirement, because it only has one double letter
(bb).

The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all 
the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next
 password be?
"""
from string import ascii_lowercase
import re



def r1(text:str)->bool:
  """
  r1 stands for requirement one. 
  From ascii_lowercase sellect straight groups of letter form abc , bcd... xyz
  and check if password containts on of them

  Parameters
  ----------
  text : str
    Password to check

  Returns
  -------
  bool
    True if first requirement is fullfilled
    False if first requirement is not fullfilled
     """
  result=False
  for i in range(len(allowed_low)-2): 
    if text.find(allowed_low[i:i+3]) != -1:
      result=True
      break
  return result

def r2(text:str)->bool:
  """
  r2 stands for requirement one. 
  Checke if "i", "l" or "o" are in the password

  Parameters
  ----------
  text;str :
    Password to check.

  Returns
  -------
  bool
    True if neither "i" nor "l" nor "o" are present

  """
  resultado=True
  for low in forbbiden_low:
    if (low in text) or ("o" in text) or ("l" in text):
      resultado= False
      break
  return resultado
  
def r3(text:str)->bool:
  """
  

  Parameters
  ----------
  text : str
    DESCRIPTION.

  Returns
  -------
  bool
    DESCRIPTION.

  """
  matcher2 = re.compile(r'(.)\1+')
  return len(tuple(matcher2.finditer(text))) >= 2

def es_valido(text:str)->bool:
  """
  

  Parameters
  ----------
  text : str
    the password to check if it meets the three requirements

  Returns
  -------
  bool
    true in all 3 requirementes are ok
    Flase otherwise.

  """
  return r1(text) and r2(text) and r3(text)

def next_lowercase(char:str)->str:
  """
  if chart is the last one of the allowed chart i return first one, else next one

  Parameters
  ----------
  char : str
    The char to increase

  Returns
  -------
  str
    DESCRIPTION.

  """
  if char == last_low:
    return allowed_low[0]
  else:
    return allowed_low[allowed_low.find(char) + 1]

  

def inc_high_order(text:str)->str:
  """
  1.- initialize last password's char to first allowed char'
  2.- from right to left i check if it is last allowed chart
    if yes i change it to fisrt  alloed letter and moved to the left
    if not i change it for the next ona and exit loop
  Parameters
  ----------
  text : str
    passwrd to increas

  Returns
  -------
  str
    increased password

  """
  
  end=len(text)-1
  text = text[:end] + allowed_low[0] #last car change for first allowed
  for i in range(end-1, -1 ,-1):
    if text[i] == last_low:
      text = text[:i] + allowed_low[0] + text[i+1:]
    else:
      text = text[:i] + next_lowercase(text[i]) + text[i+1:]
      break
  return text
  





def next_pass(text:str)->str:
  """
  i enter and infintite loop till i found a right password
  Here i change only last letter.
  When i arrive to the last allowed char i incremente hta higher order char.
  

  Parameters
  ----------
  text : str
    old password to update

  Returns
  -------
  str
    new password

  """
  i=len(text)-1
  found=False
  while not found:
    next = next_lowercase(text[i])
    if text[i] == last_low:
      text=inc_high_order(text)
    else:
      text = text[:i] + next + text[i+1:]
 
    
    found = es_valido(text)
    #print(text, found)
  return text


forbbiden_low="iol"
#allowed_low = remove_from_lowercase(forbbiden_low) with this, test2 not passed
allowed_low = ascii_lowercase
numlowercase=len(allowed_low)
last_low= allowed_low[-1]

myinput = "hxbxwxba"
test1="abcdefgh"
next_test1="abcdffaa"
test2="ghijklmn"
next_test2="ghjaabcc"

#a=next_pass("aaaaa")
print (next_pass(test1) == next_test1)
print (next_pass(test2) == next_test2)

first_next_pass=next_pass(myinput)
print ("Part one: the next password of {} is {}".format(myinput,first_next_pass))
second_next_pass=next_pass(first_next_pass)
print ("Part two: the next password of {} is {}".format(first_next_pass,second_next_pass))     

