# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:18:21 2023

@author: luism
"""
"""
This year, Santa brought little Bobby Tables a set of wires and bitwise logic 
gates! Unfortunately, little Bobby is a little under the recommended age range,
and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit 
signal (a number from 0 to 65535). A signal is provided to each wire by a gate,
another wire, or some specific value. Each wire can only get a signal from one
source, but can provide its signal to multiple destinations. A gate provides 
no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together:
x AND y -> z means to connect wires x and y to an AND gate, and then connect 
its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and  y is provided to wire z.
p LSHIFT 2 -> q means the value from  p is left-shifted by 2 and provided to q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift).

"""
"""
Approach one
i will create a simple parser to analise instructions and ejecute it
"""

"""
import re
const = re.compile(r'^([\d]+) -> ([a-z]+)$')
asign = re.compile(r'^([a-z]+) -> ([a-z]+)$')
negat = re.compile(r'^NOT ([a-z]+) -> ([a-z]+)')
binar = re.compile(r'^([a-z]+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+) -> ([a-z]+)$')
binar1 = re.compile(r'^([\d]+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+) -> ([a-z]+)$')
shift = re.compile(r'^([a-z]+) (LSHIFT|RSHIFT) ([\d]+) -> ([a-z]+)$')
wires=dict()

C=0
with open("input.txt",'r') as f:
  for line in f:
    x = const.search(line)
    if x is not None:
      C +=1
      # 0 -> c     ==>(   '0', 'c') 
      # 14146 -> b ==>('14146', 'b')
      if x.groups()[1] not in wires:
        wires.setdefault(x.groups()[1],int(x.groups()[0]))
      else:
        wires[x.groups()[1]],int(x.groups()[0])
        
    else:
      x = negat.search(line)
      if x is not None:
        C +=1
        #NOT p -> q ==> ('p', 'q')
        
        ori = wires[x.groups()[0]]
        if x.groups()[1] not in wires:
          wires.setdefault(x.groups()[1],~ori)
        else:
          wires[x.groups()[1]]= ~ori
        
      else:
        x = binar.search(line)
        if x is not None:
          C +=1
          #print(x.groups())
          pass
        else:
          x = binar1.search(line)
          if x is not None:
            C +=1
            #print(x.groups())
            pass
          else:
            x=shift.search(line)
            if x is not None:
              C +=1
              pass
            else:
              x= asign.search(line)
              if x is not None:
                C +=1
                pass
              else:
                print(line)
      

I realized that pytho eval function can simply my "instruction Analisis"

"""
print(len(dir()))
print(dir())



#import re
#const = re.compile(r'^([\d]+) -> ([a-z]+)$')
#asign = re.compile(r'^([a-z]+) -> ([a-z]+)$')
#negat = re.compile(r'^NOT ([a-z]+) -> ([a-z]+)')
#binar = re.compile(r'^([a-z]+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+) -> ([a-z]+)$')
#binar1 = re.compile(r'^([\d]+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+) -> ([a-z]+)$')
#shift = re.compile(r'^([a-z]+) (LSHIFT|RSHIFT) ([\d]+) -> ([a-z]+)$')


def subs_operators(line):
  """
  This function subtitures logical operator by python bitwise operators
  
  Firts elemente in line ia en expression to evaluate
  second element in line the assigned wire.
  
  ['cy LSHIFT 15','dc']
  is trnsformed into 
  ['cy << 15','dc']
  
  Parameters
  ----------
  line : TYPE
    The line to substitute operators
    cy LSHIFT 15 -> dc

  Returns
  -------
  TYPE
    If there is a match it returns the line with the new substring
    If there is not match return the untouched line.
    

  """
  for k,v in {"AND": "&", "OR":"|", "XOR":"^", "NOT": "65536 + ~",
              "LSHIFT": "<<", "RSHIFT":">>"}.items():
    if line.find(k) != -1:
      return line.replace(k,v)
  return line

def subs_keywords(line):
  """
  This function substitutes wires names (2 characters lengt) matching
  python reserwed words
  
  Firts elemente in line ia en expression to evaluate
  second element in line the assigned wire.
  
  ['as LSHIFT 15','if']
  is trnsformed into 
  ['my_as LSHIFT 15','my_if']
  
  Parameters
  ----------
  line : TYPE
    The line to substitute operators
    cy LSHIFT 15 -> dc

  Returns
  -------
  TYPE
    If there is a match it returns the line with the new substring
    If there is not match return the untouched line.
    

  """
  for k,v in {"as":"zz_as","if":"zz_if","in":"zz_in","is":"zz_is","or":"zz_or"}.items():
    if line.find(k) != -1 :
      return line.replace(k,v)
  return line



 
with open("input.txt",'r') as file:
  lines = file.readlines()
del file

lines= list(map(subs_operators, lines))
lines= list(map(subs_keywords, lines))

#remove "\n"
operations=list(map(lambda x:x.strip().split(' -> '),lines))





del lines,
"""
This sentence:
  
A gate provides no signal until all of its inputs have a signal.
Forces to evaluate the operations in a certain order

"""

ctrl=[] #to control if operation is evaluable
for op in operations:
  ctrl.append(False)
del op




wires={}
evaluated = ctrl.count(True)
print("Evaluated expressions {}".format(evaluated))
while not all(ctrl):
  for pos, operation in enumerate(operations):
    if not ctrl[pos]: #eval not previously evaluated instructions
      try:
        res = eval(operation[0])
        if res < 0:print("un negativo")
        ctrl[pos]= True
        globals()[operation[1]] = res
        wires[operation[1]] = res
      except:
        pass
  new_evaluated = ctrl.count(True)
  if evaluated == new_evaluated:
    break
  else:
    print("Evaluated expressions {}".format(ctrl.count(True)))
    evaluated = new_evaluated

print(globals()["a"]) 

#Part 2

operations[89][0]=str(a)
print (operations[89])

ctrl=[] #to control if operation is evaluable
for op in operations:
  ctrl.append(False)
  
for key in wires.keys():
  del globals()[key]


while not all(ctrl):
  for pos, operation in enumerate(operations):
    if not ctrl[pos]: #eval not previously evaluated instructions
      try:
        res = eval(operation[0])
        if res < 0:print("un negativo")
        ctrl[pos]= True
        globals()[operation[1]] = res
        wires[operation[1]] = res
      except:
        pass

      
print(globals()["a"]) 