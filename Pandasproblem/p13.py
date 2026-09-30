# 13. Dataset: students.csv
# Columns: Student_ID,Name,Department,Python,DBMS,Maths
# Problem Statement: Read students.csv using Pandas and perform the following:
# Display the first 5 records. 
# Display the last 5 records. 
# Find the total and average marks of each student. 
# Display students whose average marks are greater than 75. 
# Find the student with the highest average. 
# Find the average marks for each subject.
import pandas as pd
import os
folder_path = r'C:\Users\KANISHKA\OneDrive\Desktop\python sem 5\Pandasproblem'
file_path = os.path.join(folder_path, 'students.csv')  # (or employees.csv, etc.)

if not os.path.exists(file_path):
    sample_data = {
        'Student_ID': [1, 2, 3, 4, 5, 6],
        'Name': ['Kanishka', 'Manasi', 'Shraddha', 'Manjiri', 'Gauri','Gautami'],
        'Department': ['CSE', 'ECE', 'CSE', 'IT', 'CSE', 'ECE'],
        'Python': [85, 70, 95, 60, 88, 92],
        'DBMS': [80, 75, 90, 65, 85, 88],
        'Maths': [90, 80, 92, 70, 86, 95]
    }
    pd.DataFrame(sample_data).to_csv('students.csv', index=False)

df = pd.read_csv('students.csv')

print("First 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())

df['Total_Marks'] = df['Python'] + df['DBMS'] + df['Maths']
df['Average_Marks'] = df['Total_Marks'] / 3
print("\nTotal and Average marks of each student:\n", df[['Name', 'Total_Marks', 'Average_Marks']])

print("\nStudents with average marks > 75:\n", df[df['Average_Marks'] > 75])

highest_avg_student = df.loc[df['Average_Marks'].idxmax()]
print("\nStudent with the highest average:\n", highest_avg_student[['Name', 'Average_Marks']])

print("\nAverage marks for each subject:")
print("Python:", df['Python'].mean())
print("DBMS:", df['DBMS'].mean())
print("Maths:", df['Maths'].mean())