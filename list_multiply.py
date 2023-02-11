# program to print multiplication of all string elements
n = input("Enter the numbers : ")
num = list(n)
for space in num:
    if space==' ':
        num.remove(space)
mul = 1
j = 0
while j<len(num):
    mul = mul * int(num[j])
    j+=1
print(mul)