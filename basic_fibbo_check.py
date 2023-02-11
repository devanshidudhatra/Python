# program to check if the number is fibbonacci or not
num = int(input("Enter the number : "))
t1 = 0
t2 = 1
nt = t1 + t2
if num==0 or num==1:
    print("It is a fibbonacci")
    
while nt<num and num!=0 and num!=1:
    t1=t2
    t2=nt
    nt=t1+t2
    if nt==num :
        print("It is a fibonacci")
        break
    elif nt!=num :
        continue 
else:
    if num!=0 and num!=1:
        print("It is not a fibbonacci")
        