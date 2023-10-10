# program to print 2nd largest element of list
list = [ ]
n = int(input("Enter the number of elements : "))
print("Enter the list of numbers : ")
for i in range(0, n):
    ele = input()
    list.append(ele)
list.sort()
list.reverse()
print(f'Second large number is {list[1]}')    