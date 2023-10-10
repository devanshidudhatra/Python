# program to multiply two matrices

import numpy as np
r=int(input('No. of rows : '))
c=int(input('No. of columns : '))
print('Enter Array 1: ')
mat1=[]
for i in range(r):
    a=[]
    for j in range(c):
        x=int(input())
        a.append(x)
    mat1.append(a) 
print('Enter Array 2 : ')
mat2=[]
for i in range(r):
    a=[]
    for j in range(c):
        x=int(input())
        a.append(x)
    mat2.append(a)       
k=0
multi=np.empty((r,c))
for i in range(r):
    for j in range(c):
        multi[i][j]=0
        for k in range(c):
            multi[i][j]=multi[i][j]+mat1[i][k]*mat2[k][j]
print("Multiplication of array 1 and array 2 is : ")
for i in range(r):
    for j in range(c):
        print(multi[i][j],end=' ')
    print()