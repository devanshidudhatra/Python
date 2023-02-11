# program to print positive and negative NUMBERS in a list
num = [ ]
n = input("Enter the number of elements : ")
print("Enter the list of numbers : ")
for i in range(0,int(n)):
    ele = input()
    num.append(ele)
print("Positive numbers are : ")
for i in num:
    if int(i) > 0:
        print(i) 
print("Negative numbers are : ")
for i in num:
    if int(i) < 0:
        print(i)  