import pandas as pd 

df = pd.read_csv("OnlineRetail.csv", encoding="latin1")

print(df.tail())

# if you want to find out csv file rows and columns total
print(df.shape)

# find out null values

#  count of total null values 
print(df.isnull().sum().sum())

df["Description"] = df["Description"].fillna("Empty")


print(df["Description"].isnull().sum())

print("This is rows where Description is empty:")
print(df[df["Description"] == "Empty"].head())

print(df.iloc[50000:50005])


stock_code =  "22639" 
print(df[df["StockCode"] == stock_code])
print(df[df["StockCode"] == stock_code]["Quantity"].sum())

