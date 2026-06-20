import pandas as pd

# Load Datasets
df = pd.read_csv("../OnlineRetail_clean.csv")
sales_df = pd.read_csv("../sales.csv")
returns_df = pd.read_csv("../returns.csv")

# Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# ==========================================================
# Question 1: Which country generates the highest revenue?
# ==========================================================

highest_revenue_country = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(1)
)

print("\n=== Highest Revenue Country ===")
print(highest_revenue_country)

# ==========================================================
# Question 2: Identify the top 10 most sold products
# ==========================================================

top_10_products = (
    sales_df.groupby("Description")["Quantity"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
)

print("\n=== Top 10 Most Sold Products ===")
print(top_10_products)

# ==========================================================
# Question 3: Who is the most valuable customer?
# ==========================================================

most_valuable_customer = (
    sales_df.groupby("CustomerID")["Revenue"]
            .sum()
            .sort_values(ascending=False)
            .head(1)
)

print("\n=== Most Valuable Customer ===")
print(most_valuable_customer)

# ==========================================================
# Question 4: Which month generated the highest revenue?
# ==========================================================

df["Month"] = df["InvoiceDate"].dt.month_name()

highest_revenue_month = (
    df.groupby("Month")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(1)
)

print("\n=== Highest Revenue Month ===")
print(highest_revenue_month)

# ==========================================================
# Question 5: How does revenue vary month by month?
# ==========================================================

monthly_revenue = (
    df.groupby("Month")["Revenue"]
      .sum()
)

print("\n=== Month-wise Revenue ===")
print(monthly_revenue)

# ==========================================================
# Question 6: Which day of the week is the busiest?
# ==========================================================

df["Day"] = df["InvoiceDate"].dt.day_name()

busiest_day = (
    df.groupby("Day")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(1)
)

print("\n=== Busiest Day of the Week ===")
print(busiest_day)

# ==========================================================
# Question 7: How does UK revenue compare with the rest
# of the world?
# ==========================================================

uk_revenue = df[df["Country"] == "United Kingdom"]["Revenue"].sum()

rest_of_world_revenue = (
    df[df["Country"] != "United Kingdom"]["Revenue"].sum()
)

print("\n=== UK vs Rest of World Revenue ===")
print("UK Revenue:", uk_revenue)
print("Rest of World Revenue:", rest_of_world_revenue)

# ==========================================================
# Question 8: How much revenue was lost due to returns?
# ==========================================================

returned_orders = df[df["InvoiceNo"].isin(returns_df["InvoiceNo"])]

total_loss = returned_orders["Revenue"].sum()

print("\n=== Revenue Lost Due to Returns ===")
print(total_loss)

# ==========================================================
# Question 9: How many unique customers are there in each
# country?
# ==========================================================

unique_customers = (
    df.groupby("Country")["CustomerID"]
      .nunique()
      .sort_values(ascending=False)
)

print("\n=== Unique Customers by Country ===")
print(unique_customers)

# ==========================================================
# Question 10: Create a Country vs Month Revenue Pivot Table
# ==========================================================

country_month_pivot = pd.pivot_table(
    df,
    values="Revenue",
    index="Country",
    columns="Month",
    aggfunc="sum",
    fill_value=0
)

print("\n=== Country vs Month Revenue Pivot Table ===")
print(country_month_pivot)