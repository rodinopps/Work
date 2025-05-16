# This imports the pandas module to manage the data.
import pandas as pd

# This imports the numpy module for numerical operations.
import numpy as np

# This imports matplot for plotting graphs.
import matplotlib.pyplot as plt

# This imports seaborn for data visualisations.
import seaborn as sns

# Task 1
# Loads the dataset using pandas.
df = pd.read_csv("messy_dataset.csv") # This loads the dataset from the CSV file messy_dataset.
print("Messy Dataset")
print(df.head()) # This outputs the first five rows of the dataset.

# Identifies and removes any duplicate records from messy_dataset.csv.
df.drop_duplicates(inplace = True)

# This removes N/A from the Discount column with 0.
df["Discount"] = df["Discount"].replace("N/A", 0)
# This then converts the Discount column to numeric values.
df["Discount"] = pd.to_numeric(df["Discount"], errors="coerce")
# This replaces any missing values with 0.
df["Discount"].fillna(0, inplace=True)

# This converts the Date column into datetime and replacing any values that are invalid to not a numbers.
df["Date"] = pd.to_datetime(df["Date"], errors = "coerce")

# This is for the columns, Age, Sales and Profit. It is a for loop and iterates through them.
for i in ["Age", "Sales", "Profit"]:
    df[i] = pd.to_numeric(df[i], errors = "coerce") # This converts the current column to numeric values.
    df[i].fillna(df[i].median(), inplace=True) # This replaces any values that are not a number with the median value.

df["Gender"].fillna(df["Gender"].mode()[0], inplace=True) # This fills the missing values in the column which is Gender with the mode. This is the most frequent value.

df.dropna(subset=["Category"], inplace=True) # This removes any rows with no category value.

# Outlier handling for Sales column.
Q1 = df["Sales"].quantile(0.25) # This calculates the first quarter of sales.
Q3 = df["Sales"].quantile(0.75) # This calculates the third quarter of sales.
IQR = Q3 - Q1 # This calculates the interquartile range.
lower = Q1 - 1.5 * IQR # Lower bound
upper = Q3 + 1.5 * IQR # Upper bound. The lower and upper bounds are for caculating outliers.

df = df[~((df["Sales"] < (Q1 - 1.5 * IQR)) | (df["Sales"] > (Q3 + 1.5 * IQR)))] # This filters the rows where they are outside the bounds (outliers). 

# Task 2
sales_summary = df.groupby("Category")["Sales"].sum().reset_index() # This groups data by category and sum the Sales for each category. 
print(sales_summary) # This prints the summary table.

# Task 3
summary = df.describe() # This generates statistics.
print(summary) # Prints statistics.

correlation_matrix = df.select_dtypes(include = [np.number]).corr() # This calculates the correlation for columns with numbers to find the relationships.
print(correlation_matrix) # Prints matrix.

sales_pivot = df.pivot_table(values = "Sales", index = "Category", columns = "Discount", aggfunc = "sum") # This creates a table showing total sales for discounts and category.
print(sales_pivot) # Prints sales pivot table.

# Task 4

# Histogram
plt.hist(df["Sales"], bins=20, color="skyblue")
plt.title("Sales Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.show()

# Scatterplot
sns.scatterplot(x=df["Sales"], y=df["Profit"], hue=df["Category"])
plt.title("Sales vs Profit")
plt.show()

# Saves CSV file (cleaned dataset). 
df.to_csv("cleaned_dataset.csv", index=False)
# Saves summary table as CSV file.
sales_summary.to_csv("sales_summary.csv", index=False)