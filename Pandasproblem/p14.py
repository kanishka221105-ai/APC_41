# 14. Dataset: employees.csv
# Columns: Employee_ID,Name,Department,Experience,Salary
# Problem Statement: Read the CSV file and:
# Display employees from the CSE department. 
# Find the average salary. 
# Find the highest and lowest salary. 
# Display employees having salary greater than ₹50,000. 
# Calculate department-wise average salary.
import pandas as pd
import os
folder_path = r'C:\Users\KANISHKA\OneDrive\Desktop\python sem 5\Pandasproblem'
file_path = os.path.join(folder_path, 'employees.csv')  # (or employees.csv, etc.)

if not os.path.exists(file_path):
    sample_data = {
        'Employee_ID': [101, 102, 103, 104, 105],
        'Name': ['Kanishka', 'Manasi', 'Shraddha', 'Manjiri', 'Gauri'],
        'Department': ['CSE', 'ECE', 'CSE', 'IT', 'MECH'],
        'Experience': [3, 5, 2, 4, 6],
        'Salary': [45000, 65000, 48000, 70000, 55000]
    }
    pd.DataFrame(sample_data).to_csv('employees.csv', index=False)

df = pd.read_csv('employees.csv')

print("Employees from CSE department:\n", df[df['Department'] == 'CSE'])
print("\nAverage Salary:", df['Salary'].mean())
print("Highest Salary:", df['Salary'].max())
print("Lowest Salary:", df['Salary'].min())
print("\nEmployees with salary > ₹50,000:\n", df[df['Salary'] > 50000])
print("\nDepartment-wise average salary:\n", df.groupby('Department')['Salary'].mean())