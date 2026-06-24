import pandas as pd
df=pd.read_csv('Mall_Customers.csv')
#Basic exploration 
# shape function retrieves the rows and columns in format (rows,columns)
print("Shape:", df.shape)
# -> gives you the name of all columns in the csv
print("\nColumns:", list(df.columns))
# -> prints the whole value data of first 5 rows 
print("First 5 rows :")
print(df.head()) #prints the data of the row of first 5 rows by defaut


#data types should be mentioned - crucial for ml if the annual income column have a data tyoe object that means its values has dollar or ruppee sign in them preventing you from building machine learnign model . hence we have to clean it first 
print("\n Data types :")
print(df.dtypes)

#missing values - most of the machine learning models fails because of missing values hence 
#insull 
#fillna fills 0 to to the missing value SYNTAX; df.fillna(0,inplace=TRUE)
print("\n Missing Values")
print(df.isnull().sum())

print("\n Basic stats:")
print(df.describe())



print("\n- - -Buisiness Insights- - -")
print("Avg Income: ", df['Annual Income (k$)'].mean().round(1))
print("Avg Spending Score :", df["Spending Score (1-100)"].mean().round(1))
print("Average Age :",df["Age"].mean().round(1))

#Gebder Breakdown
print("\n Gender split:")
print(df['Gender'].value_counts())
# It counts the number of male and female category mentioned in csv file 

high_value = df[(df['Annual Income (k$)'] > 70) & 
                (df['Spending Score (1-100)'] > 70)]
print(f"\nHigh value customers: {len(high_value)}")
print(high_value[['Gender', 'Age', 'Annual Income (k$)', 
                   'Spending Score (1-100)']])