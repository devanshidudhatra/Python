import pandas as pd
ser1 = pd.Series(["America" , "Dubai" , "India"])
ser2 = pd.Series({"1" : "America" , "2" : "India" , "3" : "Dubai"})
print(ser1[1])
print(ser1[1:])
print(ser2['2'])