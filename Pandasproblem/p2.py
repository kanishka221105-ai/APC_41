# 2. Create a dictionary containing:
# Employee ID
# Employee Name
# Department
# Salary
# Experience
# Convert it into a Pandas DataFrame and:
# Display employees with salary greater than ₹50,000. 
# Find the average salary. 
# Find the highest salary. 
# Find the employee with the highest experience.
import pandas as pd

data = {
    'Employee ID': [101, 102, 103, 104],
    'Employee Name': ['John', 'Jane', 'Bob', 'Alice'],
    'Department': ['IT', 'HR', 'Finance', 'IT'],
    'Salary': [45000, 65000, 55000, 70000],
    'Experience': [2, 5, 3, 6]
}
df = pd.DataFrame(data)

print("Employees with salary > ₹50,000:\n", df[df['Salary'] > 50000])
print("\nAverage Salary:", df['Salary'].mean())
print("Highest Salary:", df['Salary'].max())

highest_exp_emp = df.loc[df['Experience'].idxmax()]
print("\nEmployee with the highest experience:\n", highest_exp_emp)