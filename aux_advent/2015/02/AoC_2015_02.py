# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 00:17:13 2023

@author: luism
"""

surface = 0
ribbon = 0

def calcule_paper(dim:list):
  global surface
  global ribbon
  l=dim[0]
  w=dim[1]
  h=dim[2]
  paper = 2*l*w + 2*w*h + 2*h*l + min(l*w,l*h,w*h)
  surface += paper
  dim.pop(dim.index(max(dim)))
  ribbon += 2 * sum(dim) + l*w*h
  return

  


with open("input.txt","r") as f:
    [calcule_paper(list(map(int,linea.strip().split('x')))) for linea in f.readlines()]

print("{} sqf of paper plus {} linear feets of ribbon".format(surface, ribbon))