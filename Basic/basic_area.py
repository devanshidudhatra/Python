print("                       ")
print("***********************")
print("*                     *")
print("*   r for rectangle   *")
print("*     s for square    *")
print("*   t for  triangle   *")
print("*     c for circle    *")
print("*                     *")
print("***********************")

choice = input("Whose area do u want : ")

if choice == 'r' or 'R':
    length = input("Enter length of rectangle : ")
    breadth = input("Enter breadth of rectangle :  ")
    area = int(length) * int(breadth)
    print(f'Area is {area}')
elif choice == 's' or 'S':
    side = input("Enter side of square : ")
    area = int(side) ** 2
    print(f'Area is {area}')
elif choice == 't' or 'T':
    length = input("Enter base of triangle : ")
    breadth = input("Enter height of triangle :  ")
    area = int(length) * int(breadth) * 0.5
    print(f'Area is {area}')
elif choice == 'c' or 'C':
    radius = input("Enter radius of circle")
    area = 3.14 * (int(radius)**2)
    print(f'Area is {area}')