# create pandas series from array

import pandas as pd
import numpy as np
list = ['hi' , 'hello' , 'how are u']
array = np.array(list)
series= pd.Series(array,index=[1,2,3])
print(series)