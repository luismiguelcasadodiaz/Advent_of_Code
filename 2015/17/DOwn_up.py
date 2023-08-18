# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 15:46:40 2023

@author: luism
"""
import pastel
def my_print(T):
  a=""
  for line in T:
    for e in line:
      if e:
        print(pastel.colorize("<r>T"),end="")
      else:
        print(pastel.colorize("<g>."),end="")
    print(", ",end="")
      
  print(a)
  
def subsetsum(A,k):
  
  
  n=len(A)
  T=[[False for x in range(k + 1)] for y in range(n + 1)]
  my_print(T) 
  
  for i in range(n+ 1):
    T[i][0]=True
  my_print(T)  
  for i  in range (1, n+1):
    for j in range(1, k+1):
      
      if A[i-1]>j:
        T[i][j]=T[i-1][j]
      else:
        T[i][j]=T[i-1][j] or T[i-1][j-A[i-1]]
    print(A[i-1])
    my_print(T)
  return T[n][k]


if __name__ == '__main__':
  pastel.add_style('r','magenta',options=['bold'])
  pastel.add_style('g','light_gray')
  A=[7,3,2,5,8]
  k = 18
  
  if subsetsum(A,k):
    print("Subsecuecne with the given sum exits")
  else:
    print("Subsecuecne with the given sum does exits")