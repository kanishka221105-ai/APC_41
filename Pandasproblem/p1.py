# 1. Create a dictionary containing the following information for 5 students:
# Student ID 
# Student Name 
# Python Marks 
# DBMS Marks 
# Mathematics Marks 
# Convert the dictionary into a Pandas DataFrame and:
# Display the DataFrame. 
# Calculate total marks for each student. 
# Calculate average marks. 
# Display students who scored more than 75% average.
import pandas as pd
data = {
    'Student ID': [1, 2, 3, 4, 5],
    'Student Name': ['Kanishka', 'Manasi', 'Shraddha', 'Manjiri', 'Gauri'],
    'Python Marks': [85, 70, 95, 60, 88],
    'DBMS Marks': [80, 75, 90, 65, 85],
    'Mathematics Marks': [90, 80, 92, 70, 86]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
df['Total Marks'] = df['Python Marks'] + df['DBMS Marks'] + df['Mathematics Marks']
print("\nTotal Marks for each student:\n", df[['Student Name', 'Total Marks']])
df['Average Marks'] = df['Total Marks'] / 3
print("\nAverage Marks for each student:\n", df[['Student Name', 'Average Marks']])
print("\nStudents who scored more than 75% average:\n", df[df['Average Marks'] > 75])