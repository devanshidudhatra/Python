# importing pandas package
import pandas as pd
 
# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Name")
# retrieving row by loc method
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
print(first, "\n\n\n", second)

# dropping passed columns
data.drop(["Team", "Weight"], axis = 1, inplace = True)
print("\nafter dropping columns : \n",data)

# making data frame from csv file
data = pd.read_csv("nba.csv", index_col ="Team")
  # retrieving rows by loc method
rows = data.loc["Utah Jazz"]

# checking data type of rows
print(type(rows))
# display
print(rows)
