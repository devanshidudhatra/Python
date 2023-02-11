# program to print sum of squares of n natural numbers
n = int(input("Enter the nth term : "))
temp =0
for i in range(n+1):
    num = i**2 + temp
    temp = num
print(num)