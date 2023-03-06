# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:23:10 2023

@author: luism
"""
"""
In years past, the holiday feast with your family hasn't gone so well. 
Not everyone gets along! This year, you resolve, will be different. 
You're going to find the optimal seating arrangement and avoid all those 
awkward conversations.

You start by writing up a list of everyone invited and the amount their 
happiness would increase or decrease if they were to find themselves sitting 
next to each other person. You have a circular table that will be just big 
enough to fit everyone comfortably, and so each person will have exactly 
two neighbors.

For example, suppose you have only four attendees planned, and you calculate 
their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units 
(because David talks so much), but David would gain 46 happiness units 
(because Alice is a good listener),
 for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice 
(Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob 
(Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). 
The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, 
you find that this one is the most optimal, with a total change in happiness 
of 330.

What is the total change in happiness for the optimal seating arrangement of 
the actual guest list?

I APPROACH THIS PROBLEM WIHT THE HELP OF A GRAPH

"""
import networkx as nx
import matplotlib.pyplot as plt
def get_rules()->list:
  """
  Trasts the input file.
  the input fales has rules wiht this format:
  Alice would lose 2 happiness units by sitting next to Bob.
  that is splite into a rule/list like this
  'Alice','would','lose','2','happiness',....,'next','to','Bob.']
  
  where the relevante elemente are
  rule[0] Rule owner
  rule[-1][:-1] Applies when owner sits next to him/her (Last one witho point)
  rule[2] says if there is gain or lost of hapiness
  rule[3] hapiness change
  
  

  Returns
  -------
  list
    List of rules: each rule has two names and a value:
      [rule[0], rule[-1], value]
      The value is tha hapiness changes of the first when sitted next the other

  """
  my_rules=[]
  with open("input.txt",'r') as f:
    for line in f:
      rule=line.strip().split()
      if rule[2] == 'gain':
        value = int(rule[3])
      else:
        value = - int(rule[3])
      my_rules.append([rule[0], rule[-1][:-1], value])
  return my_rules

def create_graph(rules:list):
  """
  

  Parameters
  ----------
  rules : list
    A list wiht the rules to buid up the graph
    the rules have this template ['Mallory', 'David', 91],
    The value is tha hapiness changes Mallory when sitted next David

  Returns
  -------
  my_graph : TYPE
    A graph whose edges compute the totoa change of hapiness in both guests

  """
  my_graph = nx.Graph()
  for rule in rules:
      if (rule[1],rule[0]) in my_graph.edges():
        my_graph[rule[0]][rule[1]]["h"] = rule[2] + my_graph[rule[1]][rule[0]]["h"]
      else:
        my_graph.add_edges_from([(rule[0],rule[1],{"h":rule[2]})])    
  return my_graph

def path_hapiness(G,path):
  """
  

  Parameters
  ----------
  G : TYPE
    graph wiht nodes ans edges
  path : list of nodes
    It is a path that includes all nodes.

  Returns
  -------
  happiness : TYPE
    sums up all h attirbute form the edges

  """

  b=path[1:]
  b.append(path[0])
  happiness= 0
  edges= zip(path,b) #Create edges for the path that return to first position
  for edge in edges:
    happiness += G.edges[edge]["h"]
  return happiness

def find_best_path(G):
  happiness_list = []
  num_of_nodes=G.number_of_nodes()
  for u in G.nodes:
    for v in G.nodes:
      for path in nx.all_simple_paths(G,u,v):
        if len(path)== num_of_nodes:
          happiness_list.append((path_hapiness(G,path),path))
  return  sorted(happiness_list, key=lambda x: x[0], reverse=True)
  
        
def plot_graph(G,optimus,filename):
  pathfile="C:\\Users\\luism\\OneDrive\\Proyectos\\Python Scripts\\"
  pathfile+="Advent_of_code\\2015\\13\\"+filename
  
  a=optimus
  b=optimus[1:]
  b.append(optimus[0])
  edges=zip(a,b)
  M=nx.Graph()
  for edge in edges:
    M.add_edges_from((edge[0],edge[1],{"h": G.edges[edge]["h"]}))
    
  my_labels=nx.get_edge_attributes(M,'h')
  nx.draw_networkx(M, pos=nx.circular_layout(M),font_size=20,node_size=900,
                 node_shape="d",node_color="g",width=0.1,
                 connectionstyle='arc3, rad = 0.1')
  nx.draw_networkx_edge_labels(M, nx.circular_layout(M),font_size=12, 
                             label_pos=0.5,edge_labels=my_labels)
  plt.rcParams["figure.figsize"] = [20,20]
  #plt.rcParams["figure.dpi"] = [300]
  plt.title("people at table")
  plt.draw()
  plt.savefig(pathfile)


rules=get_rules()
G=create_graph(rules)
optimus=find_best_path(G)

print("the Happiness level in this table {} is {}".format(optimus[0][1], optimus[0][0]))
plot_graph(G,optimus[0][1], "mesa.png")
