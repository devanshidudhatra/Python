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