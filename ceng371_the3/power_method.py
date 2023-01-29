
import numpy as np
def normalize(x):
    fac = abs(x).max()
    x_n = x / x.max()
    return fac, x_n
def power_method(A,v):
    #print(A)
    #A=np.linalg.inv(A) #this line is for finding the smallest eigen value
    #print(A)
    convergence=10000
    convergence_old=convergence
    iter=0
    while True:
        iter+=1
        v = np.dot(A, v)
        v_old=v
        lambda_v ,v= normalize(v)
        
        convergence_old=convergence
        convergence=abs(sum(v_old-v))
        #print(lambda_v,v)
        if convergence_old == convergence and iter>1:
            break
    return lambda_v,v


v2 = np.array([1,1,1])
A2 = np.array([[0.2,0.3,-0.5],
              [0.6,-0.8,0.2], 
              [-1.0,0.1,0.9]
              ])


A1=np.array([[2,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,0],[0,0,-1,2,-1],[0,0,0,-1,2]])
v1 = np.array([1,1,1,1,1])
                              

print(power_method(A2,v2))    