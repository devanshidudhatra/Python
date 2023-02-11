#A=P(1+r/n)^nt
# A = final amount ; P = principle amount ; r = rate of interest ; n = no. of time period elapsed ; t = time period

P = int(input("Enter the principle amount : "))
r = int(input ("Enter rate of interest : "))
n = int(input("Enter the number of times interst is applied : "))
t = int(input("Enter the time period : "))

A = (1 + r / n) ** (n*t)
A = A * P

print(f'The final amount is {A} ')