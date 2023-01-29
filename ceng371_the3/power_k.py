import numpy as np
def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n

def one_d_transpose(A):
    A1=A[0]
    A2=A[1]
    A[0]=A2
    A[1]=A1
    return A    
def power_k(A,k,v):
    convergence=10000
    convergence_old=convergence
    iter=0
    for i in range(k):
        iter+=1
        v = np.dot(A, v)
        lambda_v, v = normalize(v)
        if np.size(v)!=2:
            A=A-(lambda_v*(v*np.matrix.transpose(v))/np.matrix.transpose(v)*v)
        else:
            A=A-(lambda_v*(v*one_d_transpose(v))/one_d_transpose(v)*v)
            
        
    return lambda_v,v
        
        
    

             