# 5. Create a dictionary containing:
# Order_ID
# Customer
# Product
# Quantity
# Price
# Discount
# Create a DataFrame and calculate:
# Final Amount = Quantity × Price − Discount
# Then display:
# All orders 
# Orders above ₹5,000 
# Highest-value order 
# Average order value
import pandas as pd

data = {
    'Order_ID': [101, 102, 103, 104],
    'Customer': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Product': ['Shoes', 'Watch', 'Bag', 'Jacket'],
    'Quantity': [2, 1, 3, 1],
    'Price': [3000, 6000, 2000, 5500],
    'Discount': [200, 500, 300, 400]
}
df = pd.DataFrame(data)
df['Final Amount'] = (df['Quantity'] * df['Price']) - df['Discount']

print("All orders:\n", df)
print("\nOrders above ₹5,000:\n", df[df['Final Amount'] > 5000])
print("\nHighest-value order:\n", df.loc[df['Final Amount'].idxmax()])
print("\nAverage order value:", df['Final Amount'].mean())