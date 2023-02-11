# program to print the duplicate of the list
from collections import counter
list = []
d=[]
n = input("Enter the number of elements : ")
print("Enter the list of numbers : ")
for i in range(0,int(n)):
    ele = input()
    list.append(ele)
list.sort()
print(list)
get_duplicate(list)
# i=0
# while i<len(list):
#     j=i+1
#     while j<len(list):
#         if list[i]==list[j]:
#             d.append(list[i])
#         j+=1
#     i+=1
# d.sort()
# print(d)
# i=0
# while i<len(d):
#     if d[0]==d[1]:
#         del(d[0])
#     i+=1
# print(d)  

