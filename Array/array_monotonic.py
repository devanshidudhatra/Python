# Python Program to check if the array is monotonic or not
# An array is said to be monotonic in nature if it is either continuously increasing or continuously decreasing. 
# Mathematically, An array A is continuously increasing if for all i <= j, A[i] <= A[j].
import numpy as np
n=int(input('no. of elements:'))
li=[]
for i in range(0,n):
    e=int(input())
    li.append(e)
print(li)
l1=sorted(li,reverse=False)
l2=sorted(li,reverse=True)
print(l1)
print(l2)
if li==l1 or li==l2:
    print('monotonic array')
else:
    print('not a monotonic array')    

        