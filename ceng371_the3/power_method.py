
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


 
