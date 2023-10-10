# program to print even and odd elements in a list
num = [ ]
n = input("Enter the number of elements : ")
print("Enter the list of numbers : ")
for i in range(0,int(n)):
    ele = input()
    num.append(ele)
print("Even numbers are : ")
for i in num:
    if int(i) % 2 == 0:
        print(i) 
print("Odd numbers are : ")
for i in num:
    if int(i) % 2 != 0:
        print(i) 