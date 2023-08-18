# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 21:16:36 2023

@author: luism
"""
import networkx as nx

def path_distance(path):
    """
  

  Parameters
  ----------
  path : list of nodes
    ['Faerun', 'AlphaCentauri', 'Tambi', 'Snowdin']
  Returns
  -------
  distance : integer
    returns the sum of distances between nodes
    ['Faerun', 'AlphaCentauri']
    ['AlphaCentauri', 'Tambi']
    ['Tambi', 'Snowdin']

  """
    c= path[:-1]
    b= path[1:]
    edges = zip(c,b)
    distance = 0
    for edge in edges:
      distance += G.edges[edge]["distance"]
    return distance
  
#construction of the villages network. Weithed edges wiht the distance
G = nx.Graph()
with open("input.txt",'r') as file:
  for line in file:
    ruta, miles = line.strip().split(' = ')
    ori, dest = ruta.split(' to ')
    G.add_edge(ori, dest, distance=int(miles) )

    
#nx.draw_networkx(G)
distances_list=[]

#from all nodes to all nodes
num_of_nodes = nx.number_of_nodes(G)
for u in G.nodes:
  for v in G.nodes:
    for path in nx.all_simple_paths(G,u,v):
      if len(path) == num_of_nodes:
        distances_list.append((path_distance(path),path))


sorted_distance_list = sorted(distances_list, key=lambda x:x[0], reverse=False)
distance = min(distances_list)
  
print("part one: Small Distance is {}".format(sorted_distance_list[0][0])) 
print("part one: the path is {}".format(sorted_distance_list[0][1]))
  
print("part two: Small Distance is {}".format(sorted_distance_list[-1][0])) 
print("part two: the path is {}".format(sorted_distance_list[-1][1]))