# Python Program to find remainder of array multiplication divided by n
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
k=0
multi=np.empty((r,c))
for i in range(r):
    for j in range(c):
        multi[i][j]=0
        for k in range(c):
            multi[i][j]=multi[i][j]+mat1[i][k]*mat2[k][j]
for i in range(r):
    for j in range(c):
        print(multi[i][j],end=' ')
    print()
n=int(input('Enter the number:'))
for i in range(r):
    for j in range(c):
        print(multi[i][j]%n,end=' ')
    print()  