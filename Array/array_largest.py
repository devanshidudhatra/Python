# Python Program to find largest number of array
import numpy as np
list = []
d=[]
n = input("Enter the number of elements : ")
print("Enter the list of numbers : ")
for i in range(0,int(n)):
    ele = input()
    list.append(ele)
# for space in num:
#     if space==' ':
#         num.remove(space)
#     else:
#         space=int(space)
print(list)
arr = np.array(list)
print(arr)
print(max(arr))
