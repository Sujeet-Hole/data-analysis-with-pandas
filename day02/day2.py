import pandas as pd

# Load the dataset
df = pd.read_csv("OnlineRetail.csv", encoding="latin1")

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check data size before cleaning
print("\nShape Before Cleaning:")
print(df.shape)

# Remove rows with missing CustomerID
df.dropna(subset=["CustomerID"], inplace=True)

# Check data size after cleaning
print("\nShape After Cleaning:")
print(df.shape)

# Check if CustomerID has null values
print("\nCustomerID Null Values:")
print(df["CustomerID"].isnull().sum())

# Save cleaned data
df.to_csv("OnlineRetail_clean.csv", index=False)

# Load cleaned data again
df = pd.read_csv("OnlineRetail_clean.csv", encoding="latin1")

# Create a file for returned products
returns_df = df[df["Quantity"] < 0]

# Create a file for sales data
sales_df = df[df["Quantity"] > 0]

# Save both files
returns_df.to_csv("returns.csv", index=False)
sales_df.to_csv("sales.csv", index=False)

# Change InvoiceDate to date format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Save final cleaned data
df.to_csv("OnlineRetail_clean.csv", index=False)

print("\nWork Completed Successfully")