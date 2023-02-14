# #def isPal(n):
#     temp=0
#     j=len(n)-1
#     i=0
#     while i<len(n) and j>=0:
#         if n[i] == n[j]:
#             temp+=1
#         i+=1
#         j-=1
#     if temp == len(n):
#         print(n, " is a palindrome")
#     else :
#         print(n , " is not a palindrome.")

def isPal(str):
    str = list(str)
    rev = str[::-1]
    print(rev)
    # rev = str(rev)
    if rev==str:
        print("It is palindrome")
n = input("Enter the string : ")
isPal(n)

