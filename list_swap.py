# program to swap 2 elements in a string
n = input("Enter the numbers : ")
num = list(n)
for space in num:
    if space==' ':
        num.remove(space)
i1,i2 = input("Enter the indices of the elements that u want to exchange").split()      
temp = num[int(i1)-1]
num[int(i1)-1] = num[int(i2)-1]
num[int(i2)-1] = temp
print("Reversed list is : ")
print(num)

