# import pandas and numpy
import pandas as pd
import numpy as np
  
# series with numpy linspace() 
ser1 = pd.Series(np.linspace(3, 33, 3))
print(ser1)

# series with numpy random.normal
df=np.random.normal(0,0,10) # (Mean,variance,no.of terms)
print(df)
ser3 = pd.DataFrame(df)
print(ser3)
  
# series with numpy random.normal
ser4 = pd.Series(np.random.normal(0.0, 1.0, 5))
print("\n", ser4)
  
# series with numpy random.rand
ser5 = pd.Series(np.random.rand(10))
print("\n", ser5)

# series with numpy random.repeat
ser = pd.Series(np.repeat(0.08, 7))
print("\n", ser)