# program to print sum of a list

n = input("Enter the numbers : ")
num = list(n)
for space in num:
    if space==' ':
        num.remove(space)
sum = 0
j = 0
while j<len(num):
    sum = sum + int(num[j])
    j+=1
print(sum)