# 9. Create a Pandas Series using a dictionary containing employee names and their salaries.
# Perform:
# Display the Series. 
# Find the highest salary. 
# Find the lowest salary. 
# Calculate average salary. 
# Display employees earning more than ₹50,000.
import pandas as pd
salary_dict = {'John': 45000, 'Jane': 75000, 'Bob': 55000, 'Alice': 40000}
s = pd.Series(salary_dict)
print("Series:\n", s)
print("\nHighest salary:", s.max())
print("Lowest salary:", s.min())
print("Average salary:", s.mean())
print("\nEmployees earning more than ₹50,000:\n", s[s > 50000])