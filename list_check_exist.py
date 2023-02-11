# program to check existenc of a number in list
n = input("Enter the numbers : ")
num = list(n)
for space in num:
    if space==' ':
        num.remove(space)
find = input("Enter the numver that u want to find in list : ")
c=0
for number in num:
    if number == find:
        print(f'{find} exists in the list')
        break
    else:
        c+=1
if c==len(num):
    print(f'{find} does not exists in the list')