import pandas as pd
import numpy as np

n1 = input("Enter the numbers : ")
ser1 = list(n1)
for space in ser1:
    if space==' ':
        ser1.remove(space)
ser1 = [int(i) for i in ser1]
print(ser1)
n2 = input("Enter 2nd series : ")
ser2 = list(n2)
for space in ser2:
    if space==' ':
        ser2.remove(space)
ser2 = [int(i) for i in ser2]
print(ser2)
ser1 = pd.Series(ser1)
ser2 = pd.Series(ser2)

s = np.add(ser1,ser2)
print("Addition : \n" , s)
s = np.subtract(ser1,ser2)
print("Subtraction : \n" , s)
s = np.multiply(ser1,ser2)
print("Multiplication : \n" , s)
s = np.divide(ser1,ser2)
print("Division : \n" , s)

