def fact(n):
    if n==0 or n==1:
        return 1
    else :
        return  n * fact(n-1)

def nCr(n,r):
    return fact(n)/(fact(r) * fact(n-r))

def nPr(n,r):
    return (fact(n))/(fact(n-r))

n=int(input("Enter n : "))
r=int(input("Enter r : "))
print("nCr is : " , nCr(n,r))
print("nPr is : " , nPr(n,r))