# 3. Create a dictionary containing:
# Product ID
# Product Name
# Category
# Price
# Quantity
# Convert it into a DataFrame.
# Calculate:
# Total Amount = Price × Quantity
# Then find the product having the highest total sales.
import pandas as pd

data = {
    'Product ID': [1, 2, 3],
    'Product Name': ['Laptop', 'Mouse', 'Keyboard'],
    'Category': ['Electronics', 'Accessory', 'Accessory'],
    'Price': [50000, 500, 1500],
    'Quantity': [5, 50, 20]
}
df = pd.DataFrame(data)
df['Total Amount'] = df['Price'] * df['Quantity']
print("DataFrame with Total Amount:\n", df)

highest_sales_product = df.loc[df['Total Amount'].idxmax()]
print("\nProduct with the highest total sales:\n", highest_sales_product)