# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:10:14 2021

@author: cleiton
"""

import numpy as np
from scipy.linalg import inv


import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

# np.set_printoptions(precision=3)

# Variação total
def d_tv(u,v):
    tv = 0.5*((np.abs(u-v)).sum())
    return tv

# ------------------------------------------------
# Grafo 1 - Anel
# ------------------------------------------------
n1 = 100
G1 = nx.circulant_graph(n1,range(1,2))
#nx.draw(G1)

# Matriz de transição de probabilidade
A1 = nx.adjacency_matrix(G1).todense()
d1 = [d for _, d in G1.degree]
D1 = np.diag(d1)
I1 = np.identity(n1)
P1 = 0.5*(I1+inv(D1)@A1)

# Distribuição estacionária
pi_est1 = np.array([1/n1]*n1)

# pi(0)
pi1 = np.zeros((1,n1))
pi1[0][0] = 1 


# ------------------------------------------------
# Grafo 2 - Árvore
# ------------------------------------------------

G2 = nx.balanced_tree(2, 6)
#pos = graphviz_layout(G, prog="dot")
#nx.draw(G2, pos, node_size=5, with_labels=True)
#plt.show()

n2 = len(G2)
A2 = nx.adjacency_matrix(G2).todense()
d2 = [d for _,d in G2.degree]
D2 = np.diag(d2)
I2 = np.identity(n2)
P2 = 0.5*(I2+inv(D2)@A2)

pi2 = np.zeros((1,n2))
pi2[0][0] = 1 

def Prob2(i):
    if i==0:
        return 1/126
    elif 0 < i < 63: 
        return 1/84
    else:
        return 1/252
pi_est2 = np.array([Prob2(i) for i in range(n2)])


# ------------------------------------------------
# Grafo 3 - Grid 2D
# ------------------------------------------------
n3 = 100
G3 = nx.grid_2d_graph(10, 10)
#pos = {(x,y):(y,-x) for x,y in G3.nodes()}
#nx.draw(G3, pos, with_labels=True)

A3 = nx.adjacency_matrix(G3).todense()
d3 = [d for _,d in G3.degree]
D3 = np.diag(d3)
I3 = np.identity(n3)
P3 = 0.5*(I3+inv(D3)@A3)

pi3 = np.zeros((1,n3))
pi3[0][0] = 1 

def Prob3(v):
    i,j=v
    if v in {(0,0),(0,9),(9,0),(9,9)}:
        return 1/180
    elif j==0 or j==9 or i==0 or i==9:
        return 1/120
    else:
        return 1/90
        
pi_est3 = np.array([Prob3(v) for v in G3.nodes])


# ------------------------------------------------
# Gráficos - Variação total
# ------------------------------------------------
T = 10000
tv1 = []
tv2 = []
tv3 = []
for t in range(T):
    pi1 = pi1@P1
    pi2 = pi2@P2
    pi3 = pi3@P3    
    tv1.append(d_tv(pi1, pi_est1))
    tv2.append(d_tv(pi2, pi_est2))
    tv3.append(d_tv(pi3, pi_est3))

plt.figure()
plt.plot(tv1, label='Anel')
plt.plot(tv2, label='Árvore')
plt.plot(tv3, label='Grid 2D')

plt.xlabel(r'$t$')
plt.ylabel(r'$d_{TV}$')
plt.yscale('log')
plt.xscale('log')
plt.legend()