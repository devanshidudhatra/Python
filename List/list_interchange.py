#program to interchange 1st and last element of a list
n = input("Enter the numbers : ")
num = list(n)
for space in num:
    if space==' ':
        num.remove(space)
temp = num[0]
num[0] = num[len(num)-1]
num[len(num)-1] = temp
print("Reversed list is : ")
print(num)

