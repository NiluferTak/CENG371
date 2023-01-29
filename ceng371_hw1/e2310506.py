from math import floor
import sys
import numpy as np

import matplotlib as plt
from matplotlib import pyplot as pllt
from pyparsing import nums

def fn(x):
    y = x*(((x+1)/x) -1) -1
    return y


def gn(x):
    ep = sys.float_info.epsilon
    y=fn(x)/ep
    
    return y


xvals=np.linspace(1,1000,1000)
yvals=list(map(gn,xvals))

pllt.plot(xvals,yvals)


for i in range(0,len(yvals)):
    if yvals[i]==0:
        print(xvals[i])

def numsarray(n):
    iterator=0
    total=0
    nums = [1+(1000000+1-x)*0.00000001 for x in range(1,n+1)] 
    
    return nums    

   
def naivesummation(nums):
    iterator = 0
    total=0
    while iterator < len(nums):
        total = (total + nums[iterator])
        iterator += 1
    return total   

def compensationsummation(nums):
    sum =0.0
    c=0.0
    for i in range(0,len(nums)):
        y=(nums[i])-c 
        t=(sum+y)
        c=((t-sum)-y)
        sum=(t)
    return (sum)    





def pairwisesummation(x):
    #s = pairwisesummation(x)
    if len(x) <=1:
        s=0
        for i in range(0,len(x)):
            s=s+(x[i])
          
    else:
        m=floor(len(x)/2)
              
        s=(pairwisesummation(x[0:m])) + (pairwisesummation(x[m:len(x)]))
    return s    





####FGETTING THE RESULTS####
#pllt.show()
#
#
nums=numsarray(1000000)
#print(pairwisesummation(nums))
#print(np.float32(pairwisesummation(nums)))
#print(compensationsummation(nums)) 
#print(np.float32(compensationsummation(nums))) 
#print(naivesummation(nums))
#print(np.float32(naivesummation(nums)))




#########Q2c########
####double precision
#naive = 1005000.0049999995  [Done] exited with code=0 in 7.371 seconds
#compensation=1004998.995 [Done] exited with code=0 in 2.731 seconds
#pairwise=1005000.0049999999 [Done] exited with code=0 in 3.813 seconds
#print(sys.float_info.epsilon)
####single precision####
#pairwise=1005000.0  [Done] exited with code=0 in 5.424 seconds
#compensation=1005000.0 [Done] exited with code=0 in 2.872 seconds
#naive=1005000.0  [Done] exited with code=0 in 2.54 seconds