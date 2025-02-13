# -*- coding: utf-8 -*-

def subs_operators(line):
  for k,v in {"AND": "&", "OR":"|", "XOR":"^", "NOT": "65536 + ~",
              "LSHIFT": "<<", "RSHIFT":">>"}.items():
    if line.find(k) != -1:
      return line.replace(k,v)
  return line

def subs_keywords(line):
  for k,v in {"as":"zz_as","if":"zz_if","in":"zz_in","is":"zz_is","or":"zz_or"}.items():
    if line.find(k) != -1 :
      return line.replace(k,v)
  return line
 
with open("input2.txt",'r') as file:
  lines = file.readlines()


lines= list(map(subs_operators, lines))
lines= list(map(subs_keywords, lines))
operations=list(map(lambda x:x.strip().split(' -> '),lines))

ctrl=[] #to control if operation is evaluable
for op in operations:
  ctrl.append(False)

while not all(ctrl):
  for pos, operation in enumerate(operations):
    if not ctrl[pos]: #eval not previously evaluated instructions
      try:
        res = eval(operation[0])
        ctrl[pos]= True
        globals()[operation[1]] = res
      except:
        pass

print(globals()["a"])