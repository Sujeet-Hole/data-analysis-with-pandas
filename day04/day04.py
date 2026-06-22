
import pandas as pd


df = pd.read_csv("../OnlineRetail_clean.csv")


# ==================================
# FIND LAST PURCHASE OF EACH CUSTOMER
# ==================================

# Group data by CustomerID
# Find the latest purchase date for each customer
last_purchase = df.groupby("CustomerID")["InvoiceDate"].max()

print("Last purchase date of each customer:")
print(last_purchase)


# ==================================
# FIND DETAILS OF ONE CUSTOMER
# ==================================

# Select a customer ID
customer_id = 12346

# Find the last purchase date of this customer
last_purchase = df[df["CustomerID"] == customer_id]["InvoiceDate"].max()

print("\nLast purchase date of customer 12346:")
print(last_purchase)


# ==================================
# FIND ORDER FREQUENCY
# ==================================

# Count unique invoice numbers
# This shows how many orders the customer made
order_frequency = df[df["CustomerID"] == customer_id]["InvoiceNo"].nunique()

print("\nTotal orders:")
print(order_frequency)


# ==================================
# FIND TOTAL SPENDING
# ==================================

# Add all revenue values of the customer
# This shows total money spent
total_spending = df[df["CustomerID"] == customer_id]["Revenue"].sum()

print("\nTotal spending:")
print(total_spending)


# ==================================
# CONVERT DATE COLUMN
# ==================================

# Convert InvoiceDate from text to datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])


# ==================================
# FIND SNAPSHOT DATE
# ==================================

# Get the latest date in the dataset
# This date is used to calculate Recency
snapshot_date = df["InvoiceDate"].max()


# ==================================
# CREATE RFM TABLE
# ==================================

# Group data by CustomerID
# Recency  = Days since last purchase
# Frequency = Total unique orders
# Monetary = Total money spent

rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Revenue": "sum"
})


# Rename column names
rfm.columns = ["Recency", "Frequency", "Monetary"]


# ==================================
# SHOW FIRST 5 ROWS OF RFM TABLE
# ==================================

print("\nRFM Table:")
print(rfm.head())