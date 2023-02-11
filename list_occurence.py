# program to check the occurence of a element in a list
num = []
n = input("Enter the number of elements of list : ")
list = input("Enter the list : ")
for i in range(int(n)):
    num=list
repeat = input("enter the number whose occurence u want to find : ")
c=0
for number in num:
    if number == repeat:
        c+=1
        continue
print(f'{repeat} occurs {c} times')