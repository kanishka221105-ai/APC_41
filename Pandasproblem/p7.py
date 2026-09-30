# 7. A retail shop maintains sales information in a Python dictionary containing Product_ID, Product_Name, Category, Price, and Quantity.
# Write a Python program to:
# Convert the dictionary into a Pandas DataFrame. 
# Add a new column Total_Sales. 
# Calculate the total sales using Price × Quantity. 
# Display products with sales greater than ₹10,000. 
# Find the product with maximum sales. 
# Calculate the average sales.[cite: 2]
import pandas as pd

data = {
    'Product_ID': [101, 102, 103, 104],
    'Product_Name': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessory'],
    'Price': [40000, 20000, 15000, 8000],
    'Quantity': [1, 2, 1, 2]
}
df = pd.DataFrame(data)
df['Total_Sales'] = df['Price'] * df['Quantity']

print("Products with sales greater than ₹10,000:\n", df[df['Total_Sales'] > 10000])
print("\nProduct with maximum sales:\n", df.loc[df['Total_Sales'].idxmax()])
print("\nAverage sales:", df['Total_Sales'].mean())