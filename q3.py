# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 21:14:29 2021

@author: cleiton
"""

from math import log

p = 0.75
n = 10

def pi(i):
    if i in range(1,n):
        return (1-p)*p**(i-1)
    else:
        return p**(i-1)


e = 10**-6
def delta(pi0):
    t = log(1/(pi0*e))
    return t
    
P = [pi(i) for i in range(1,n+1)]
Pi0 = [1.8147e-6, 1.9531e-3, 2.5028e-2]

T = [delta(pi0) for pi0 in Pi0]