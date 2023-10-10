# Program to print nth fibbonacci of the series
n = int(input("Enter n : "))
t1 = 0
t2 = 1
nt = t1 + t2

for i in range(4,n+1):
    t1=t2                                                  
    t2=nt
    nt=t1+t2
else:
    print(nt)

def fibo(n):
    if n <= 0:
        return None  # undefined for negative or zero inputs
    elif n == 1:
        return 0  # first Fibonacci number is 0
    elif n == 2:
        return 1  # second Fibonacci number is 1
    else:
        # calculate the nth Fibonacci number using recursion
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter a positive integer: "))
result = fibo(n)
print(result)