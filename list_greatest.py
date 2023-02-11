n = input("Enter the numbers : ")
num = list(n)
for space in num:
    if space==' ':
        num.remove(space)
print(num)
max = num[0]
for number in num:
    if number > max:
        max = number
print("Maximum number is : ")
print(max)