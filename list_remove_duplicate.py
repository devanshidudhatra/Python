# program to remove duplicate from a list
list = []
l1 = []
n = input("Enter the number of elements : ")
print("Enter the list of numbers : ")
for i in range(0,int(n)):
    ele = input()
    list.append(ele)

list.sort()

print(list)

for i in list :
    if i not in l1 :
        l1.append(i)
# for i in range(0,len(list)) :
#     if(list[i]==list[i-1]) :
#         # list.remove(list[i])
#         # l1.replace(list(i))
#         l1[i] = list[i]
print(l1)
            

    
