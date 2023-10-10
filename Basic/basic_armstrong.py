num = input("Enter a three digit number : ")
if len(num) == 3 :
    temp = (int(num[0]) ** 3) + (int(num[1]) ** 3) + (int(num[2]) ** 3)
    if temp == int(num) :
        print(f'{num} is a armstrong number ')
    else:
        print(f'{num} is not a armstrong number')
else:
    print("Enter 3 digit number only")
