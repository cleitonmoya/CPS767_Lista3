# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 23:10:24 2021
@author: cleiton
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 8})

#
# Funções auxiliares
#

# Realiza movimento
def movimento(s0,D,pD):
    
    i,j = s0
    
    # sorteia a direção
    d = np.random.choice(D,p=pD)
    
    # calcula o novo estado
    if d=='N':
        s = (i+1,j)
    elif d=='L':
        s = (i,j+1)
    elif d=='S':
        if i > 1:
            s = (i-1,j)
        else:
            s = s0
    elif d=='O':
        if j > 1:
            s = (i,j-1)
        else:
            s = s0 
    return s,d

# Calcula a distância de Manhattan
def dist(s):
    i,j = s
    d = (i-1) + (j-1)
    return d

#
# Parâmetros da simução
#
N = 1000                  # número de simulações 
P = [0.25, 0.35, 0.45]    # probabilidades de transição
TT = []                   # tau_ii

#
# Simulação
#

np.random.seed(42)
for p in P:

    pN = pL = p/2
    pS = pO = (1-p)/2
    
    D = ['N','L','S','O']
    pD = [pN, pL, pO, pS]    
        
    T = []
    for n in range(N):
    
        s0 = (1,1)
        s = None
        t = 0
        while s != (1,1):
            s,d = movimento(s0,D,pD)
            s0 = s
            t = t+1
        T.append(t)
    TT.append(T)
    tau_mean = np.array(T).mean()
    tau_std = np.array(T).std()
    print(f'p{p}: Tau_11 = {tau_mean:.3f} ± {tau_std:.3f}')

# Resultados

fig,ax = plt.subplots(3, 1)
for i,p in enumerate(P):
        T = TT[i]
        t,c = np.unique(T, return_counts=True)
        ax[i].set_title(f'p={p}')
        ax[i].bar(t,c,alpha=0.7)
        ax[i].axvline(x=np.array(T).mean(),c='r',linestyle='--', label='média')
        ax[i].set_xlabel(r'$\tau_{11}$')
        ax[i].set_yscale('log')
        ax[i].set_xscale('log')
        ax[i].set_xlim([8*10**-1, 10**3])
        ax[i].set_ylim([8*10**-1, N])
        if i==0:
            ax[i].legend()
plt.tight_layout()