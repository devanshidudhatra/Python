# Program to vertically concatenate two arrays
import numpy as np
l1=[]
l2=[]
l1 = list(input("Enter first array : "))
l2 = list(input("Enter second array : "))
print(l1,"\n",l2)
arr1 = np.array(l1)
arr2 = np.array(l2)
print(arr1,"\n",arr2)
arr = np.concatenate((arr1,arr2))
print(arr)
