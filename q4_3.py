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
N = 10000                  # número de simulações 
P = [0.25, 0.35, 0.45]    # probabilidades de transição
TT = [10, 100, 1000]      # número de passos por simulação

SSS = [] # últimos estados
MMM = [] # distância de Manattan

#
# Simulação
#

np.random.seed(42)
for p in P:

    pN = pL = p/2
    pS = pO = (1-p)/2
    
    D = ['N','L','S','O']
    pD = [pN, pL, pO, pS]    
    
    SS = []
    MM = []
    for T in TT:
    
        S = []
        M = []
        for n in range(N):
        
            s0 = (1,1)   
            for t in range(T):
                s,d = movimento(s0,D,pD)
                s0 = s
            
            # Armazena o último estado
            S.append(s) 
           
            # Distância de Manhattan
            M.append(dist(s))
        
        SS.append(S)
        MM.append(M)
        d_mean = np.array(M).mean()
        d_std = np.array(M).std()
        print(f'p{p}, T{T}: Distância média: {d_mean:.3f} ± {d_std:.3f}')

    SSS.append(SS)
    MMM.append(MM)

#
# Resultados
#

x_lim = [10, 20, 40]
fig,ax = plt.subplots(3, 3)
for i,p in enumerate(P):
    for j,t in enumerate(TT):
        M = MMM[i][j]
        d,c = np.unique(M, return_counts=True)
        ax[i,j].set_title(f'p={p}, t={t}')
        ax[i,j].bar(d,c,alpha=0.7)
        if i==2:
            ax[i,j].set_xlabel('Dist. Manhattan')
        if j==0:
            ax[i,j].set_ylabel('Freq.')  
plt.tight_layout()