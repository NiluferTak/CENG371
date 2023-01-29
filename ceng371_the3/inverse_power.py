from cmath import sqrt
import numpy as np
def shifted_inverse_power_method(A,v,a):
    
    z=((np.size(A))**1/2)
    z=int(z)
    A=np.linalg.pinv(np.dot((A-a),np.identity(z)))
    convergence=10000
    convergence_old=convergence
    iter=0
    while True:
        iter+=1
        v = np.dot(A, v)
        v_old=v
        lambda_v = abs(v).max()
        v = v / v.max()
        convergence_old=convergence
        convergence=abs(sum(v_old-v))
        if convergence_old == convergence and iter>1:
            break
    return lambda_v,v

     