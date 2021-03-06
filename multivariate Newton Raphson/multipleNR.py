# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 14:38:44 2022

@author: faruukkamis
"""

import numpy as np
from sympy import Symbol, lambdify

def f1(x1,x2,x3):
    return x1*x2*x3**2 - 4.326*x2*x3**2 - (x1**2)*x2 - 8.652*x1*x2 - 24.714*x2 + 37.289

def f2(x1,x2,x3): 
    return x2*x3 + 47.593*x2 - x1 + 4.326

def f3(x1,x2,x3):   
    return -x3 + x1**2 - 8.652*x1 - 28.879

# defining symbols to derive with respect to them.
x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')

# derivation of functions.
# f11 means that derivative of f1 with respect to x1.
f11 = lambdify([x1,x2,x3],f1(x1,x2,x3).diff(x1))
f12 = lambdify([x1,x2,x3],f1(x1,x2,x3).diff(x2))
f13 = lambdify([x1,x2,x3],f1(x1,x2,x3).diff(x3))

f21 = lambdify([x1,x2,x3],f2(x1,x2,x3).diff(x1))
f22 = lambdify([x1,x2,x3],f2(x1,x2,x3).diff(x2))
f23 = lambdify([x1,x2,x3],f2(x1,x2,x3).diff(x3))

f31 = lambdify([x1,x2,x3],f3(x1,x2,x3).diff(x1))
f32 = lambdify([x1,x2,x3],f3(x1,x2,x3).diff(x2))
f33 = lambdify([x1,x2,x3],f3(x1,x2,x3).diff(x3))

P = np.array([10,2,10])             #Initial Points.
J = np.empty([3,3])     # Jacobien matrix.
F = np.ones(3)          # Solution matrix.
tr_F = F.transpose()    # transpose of solution matrix.
max_itr = 1000        # maximum iteration.
num_itr = 0             # number of iteration.
TOL = 0.0001             # tolerance.
P1 = np.ones(3)

while max(abs(F)) > TOL or num_itr < 1:
    
    if max_itr - num_itr < 0:   # to control loop.
        print('---maximum iteration was reached and roots could not find.---')
        break
    
    for i in range(len(P)):         # loop for rows of Jacobien matrix and F.
        
        for j in range(len(P)):     # loop for columns of Jacobien matrix.
            if i ==0:
                F[i] = f1(P[0],P[1],P[2])
                if j ==0:    
                    J[i][j] = f11(P[0],P[1],P[2])
                if j == 1:
                    J[i][j] = f12(P[0],P[1],P[2])
                if j ==2:
                    J[i][j] = f13(P[0],P[1],P[2])
            if i ==1:
                F[i] = f2(P[0],P[1],P[2])
                if j ==0:    
                    J[i][j] = f21(P[0],P[1],P[2])
                if j == 1:
                    J[i][j] = f22(P[0],P[1],P[2])
                if j ==2:
                    J[i][j] = f23(P[0],P[1],P[2])            
            if i ==2:
                F[i] = f3(P[0],P[1],P[2])
                if j ==0:    
                    J[i][j] = f31(P[0],P[1],P[2])
                if j == 1:
                    J[i][j] = f32(P[0],P[1],P[2])
                if j ==2:
                    J[i][j] = f33(P[0],P[1],P[2]) 
                    
    num_itr = num_itr + 1           
    inv_J = np.linalg.inv(J)        # inverse of Jacobien matrix.
    P = P - np.matmul(inv_J,F)      # N-R method. 
         

if max(abs(F)) < TOL:
    print('Roots: \nx1 =',P[0], '\nx2 =',P[1], '\nx3 =',P[2] ,'\niteration =',num_itr )







