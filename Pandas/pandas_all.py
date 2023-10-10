import pandas as pd
import numpy

c=pd.Categorical({"NAme":"Dev","salary":"2000000"})
print(c) # shows the categories and datatypes of all the values in list
# ---------------------------------------------------------------------
s1=pd.Series([3,"apple"],[2,"mango"])
s2=pd.Series([5,"banana"],[1,"pineapple"])
print(pd.concat([s1,s2],join='outer'))
# ------------------------------------------------------------------------
a = numpy.array(["foo", "foo", "foo", "foo",
                 "bar", "bar", "bar", "bar",
                 "foo", "foo", "foo"],
                dtype=object)
  
b = numpy.array(["one", "one", "one", "two",
                 "one", "one", "one", "two",
                 "two", "two", "one"],
                dtype=object)
  
c = numpy.array(["dull", "dull", "shiny",
                 "dull", "dull", "shiny",
                 "shiny", "dull", "shiny",
                 "shiny", "shiny"],
                dtype=object)
print(pd.crosstab(a, [c,b], rownames=['a'], colnames=['c','b'])) # crosstab will combine the data and is mainly used for comparision and analysis
# ------------------------------------------------------------------------------------------
pd.cut
# -------------------------------------------------------------------------------------------
print(pd.date_range(start="1/1/2004",end="8/1/2004",periods=8,))
# -------------------------------------------------------------------------------------------
print(pd.describe_option())
# --------------------------------------------------------------------------------------------
print(pd.factorize([2,3]))