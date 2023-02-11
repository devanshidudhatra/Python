num = input("Enter the number whose factorial u want : ")
i=1
fact = 1
while i <= int(num) :
    fact = fact * i
    i=i+1
print(f'Factorial of {num} is {fact}')