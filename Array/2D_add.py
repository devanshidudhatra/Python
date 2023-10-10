# program to add two matrices

import numpy as np
r=int(input('no. of rows'))
c=int(input('no. of columns'))
print('array1')
mat1=[]
for i in range(r):
    a=[]
    for j in range(c):
        x=int(input())
        a.append(x)
    mat1.append(a) 
for i in range(r):
    for j in range(c):
        print(mat1[i][j],end=' ')
    print()
print('array2')
mat2=[]
for i in range(r):
    a=[]
    for j in range(c):
        x=int(input())
        a.append(x)
    mat2.append(a) 
for i in range(r):
    for j in range(c):
        print(mat2[i][j],end=' ')
    print()        
print("Addition of two matrices is : ")
for i in range(r):
    for j in range(c):
        print(mat1[i][j] + mat2[i][j],end=' ')
    print()  