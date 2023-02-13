def is_prime(n):
    if n<1:
        print("invalid")
    elif n==1 :
        return 0
    else:
        for i in range(2,int((n/2)+1)):
            if n%i == 0:
                return 0
                break 
        else:
            return 1
        
n = int(input("Enter the number : "))
print(is_prime(n))