# Import pandas library
# Pandas is used to work with data tables
import pandas as pd


# Read CSV file
df = pd.read_csv("h.csv")


# =========================
# BASIC DATA EXPLORATION
# =========================

# Show first 5 rows
print(df.head())

# Show last 5 rows
print(df.tail())

# Show total rows and columns
print(df.shape)

# Show statistics of numeric columns
print(df.describe())

# Show all column names
print(df.columns)

# Show marks column
print(df["marks"])


# =========================
# FILTERING DATA
# =========================

# Show students with marks greater than 80
print(df[df["marks"] > 80])

# Show students with age less than average age
print(df[df["age"] < df["age"].mean()])

# Show students with age greater than 20
print(df[df["age"] > 20])

# Show students with marks between 70 and 90
print(df[(df["marks"] >= 70) & (df["marks"] <= 90)])


# =========================
# GROUP BY OPERATIONS
# =========================

# Find average marks for each year
print(df.groupby("year")["marks"].mean())

# Find average marks for each year and sort in descending order
print(
    df.groupby("year")["marks"]
      .mean()
      .sort_values(ascending=False)
)

# Find maximum marks in each year
print(df.groupby("year")["marks"].max())

# Count students in each year
print(df.groupby("year").size())


# =========================
# SORTING
# =========================

# Sort data by city name
print(df.sort_values(by="city", ascending=True))


# =========================
# DATA INFORMATION
# =========================

# Show dataset information
print(df.info())


# =========================
# HEAD AND TAIL PRACTICE
# =========================

# Show first 3 rows
print(df.head(3))

# Show last 2 rows
print(df.tail(2))


# =========================
# MARKS ANALYSIS
# =========================

# Find average marks
print(df["marks"].mean())

# Find highest marks
print(df["marks"].max())

# Find lowest marks
print(df["marks"].min())

# Find median marks
print(df["marks"].median())


# =========================
# COUNTING DATA
# =========================

# Count students in each year
print(df["year"].value_counts())

# Count total student IDs
print(df["student_id"].value_counts().sum())

# Count rows
print(df.shape[0])

# Count columns
print(df.shape[1])

# Count students with age 21
print(df[df["age"] == 21].shape[0])

# Count students with marks greater than 75
print((df["marks"] > 75).sum())

# Count students with marks greater than 80
print((df["marks"] > 80).sum())

# Count students with age less than or equal to 20
print(df[df["age"] <= 20].shape[0])

# Count students in year 3
print((df["year"] == 3).sum())


# =========================
# ABOVE AND BELOW AVERAGE
# =========================

# Students with marks greater than average
above_avg = df[df["marks"] > df["marks"].mean()]
print(above_avg.shape[0])

# Students with marks less than average
below_avg = df[df["marks"] < df["marks"].mean()]
print(below_avg.shape[0])

# Students with marks greater than or equal to 70
good_students = df[df["marks"] >= 70]
print(good_students.shape[0])

# Students with exactly 80 marks
exact_marks = df[df["marks"] == 80]
print(exact_marks.shape[0])


# =========================
# TOPPER OF EACH YEAR
# =========================

# Find highest marks in every year
top_marks = df.groupby("year")["marks"].max()

# Find students who got those marks
topper = df[df["marks"].isin(top_marks)]

print(topper)


# =========================
# AGE ANALYSIS
# =========================

# Find minimum age
print(df["age"].min())

# Find maximum age
print(df["age"].max())

# Find average age
print(df["age"].mean())

# Find average marks of students older than 20
print(df[df["age"] > 20]["marks"].mean())


# =========================
# NULL VALUE ANALYSIS
# =========================

# Check null values in each column
print(df.isnull().sum())

# Fill null values in marks column with average marks
df["marks"] = df["marks"].fillna(df["marks"].mean())

# Show percentage of null values in each column
print(df.isnull().mean() * 100)