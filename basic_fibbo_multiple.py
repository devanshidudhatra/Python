#Given two integers n and k. Find position the nth multiple of K in the Fibonacci series. 
#Examples:

#Input: k = 2, n = 3
#Output: 9, 3rd multiple of 2 in Fibonacci Series is 34 that appears at position 9.

#Input: k = 4, n = 5 
#Output: 30, 5th multiple of 4 in Fibonacci Series is 832040 which appears at position 30.

num = int(input("Enter the number : "))
mul = int(input("Enter the index of multiple u want : "))
t1 = 0
t2 = 1
nt = t1 + t2
temp = 0
i=2
while i>0 :
    t1=t2
    t2=nt
    nt=t1+t2
    i+=1
    if nt % num == 0:
        temp+=1
        if temp == mul:
            print(i)


