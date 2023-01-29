

from scipy import linalg
import numpy as np

def subspace_iterations(A,k):
    
    V,R=linalg.qr(V,0)
    for i in range(k):
        V,R=linalg.qr(A*V,0)
        Ak=np.matrix.transpose(V)*A*V


    return Ak,V    
