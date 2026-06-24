import pandas as pd

# read the csv file 
df = pd.read_csv("Mall_Customers.csv")

#print the row count 
print(f"Number of rows:{len(df)}")

#print count of columns 
print(f"Number of columns{len(df.columns)}")

#Bonus - peak at data 
print(df.head())

print(df.shape)