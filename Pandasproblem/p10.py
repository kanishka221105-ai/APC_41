#9.	Create a Pandas Series using a dictionary containing product names and prices.
# Perform:
# •	Display all products and prices. 
# •	Increase every price by 10%. 
# •	Find the most expensive product. 
# •	Find products costing more than ₹1,000.
import pandas as pd

price_dict = {'Laptop': 45000, 'Mouse': 500, 'Keyboard': 1200, 'Monitor': 8000}
s = pd.Series(price_dict)

print("All products and prices:\n", s)
s_increased = s * 1.10
print("\nPrices increased by 10%:\n", s_increased)
print("\nMost expensive product:", s.idxmax(), "with price", s.max())
print("\nProducts costing more than ₹1,000:\n", s[s > 1000])