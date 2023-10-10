# Python3 code to demonstrate
# matrix creation of n * n
# using list comprehension
import numpy as np
arr1 = np.arange(1,10,2)
print(arr1)
n = int(input("Enter the dimension of matrix : "))
arr2 = np.full((n,n),8)
print(arr2)
print(np.empty((1,)))
print(np.zeros((2,),order='C'))
print(np.ones((2,3),order='F'))
print(np.linspace(1,10,7))
print(np.copy(arr2))
print(np.reshape(arr1,(1,5)))