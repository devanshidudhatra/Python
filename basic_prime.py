min_lim = input("Enter the range in which u want prime numbers : ")
max_lim=input("max lim")
print("Prime numbers are : ")
n = int(min_lim)
while n <= int(max_lim):
    i=2
    C=0
    while i < n:
        if n % i == 0:
           C+=1
        i+=1
    if C==0:
        print(n)            
    n+=1
    
            
