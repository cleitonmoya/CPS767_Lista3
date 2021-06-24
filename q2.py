# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:10:14 2021

@author: cleiton
"""

import numpy as np
from numpy import log2
from scipy.linalg import inv, eig


import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

np.set_printoptions(precision=3)


T = nx.balanced_tree(2, 6)
pos = graphviz_layout(T, prog="dot")
nx.draw(T, pos, node_size=5, with_labels=True)
plt.show()

'''
# 2.1 - Grafo em anel

def P_Anel(i,j):
    if j==i:
        return 1/2 
    elif j == i+1:
        return 1/4 
    elif j == i-1:
        return 1/4 
    elif j == 0 and i==5:
        return 1/4 
    elif j== 5 and i==0:
        return 1/4
    else:
        return 0

P = [[P_Anel(i,j) for j in range(6)]
     for i in range(6)]
P = np.array(P)
print(P)

# 2.2 Árvore binária
n = 7

def P_bin(i,j,n):
    if j==i:
        return 1/2
    elif (i==1 and (j==2 or j==3)):
        return 1/4
    elif (j==2*i or j == 2*i+1 or j==i//2) and i < (n+1)/2:
        return 1/6
    elif (i>= (n+1)/2 and j>= (n+1)/4 and j==i//2):
        return 1/2
    else:
        return 0
    
P2 = [[P_bin(i,j,n) for j in range(1,n+1)]
      for i in range(1,n+1)]
P2 = np.array(P2)
print(P2)
'''