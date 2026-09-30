# 6. Create a dictionary containing:
# Student_ID
# Name
# Department
# Total_Classes
# Classes_Attended
# Create a DataFrame and calculate:
# Attendance Percentage = (Classes_Attended / Total_Classes) × 100
# Display students whose attendance is below 75%.
import pandas as pd

data = {
    'Student_ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Department': ['CSE', 'ECE', 'IT', 'CSE'],
    'Total_Classes': [50, 50, 50, 50],
    'Classes_Attended': [40, 30, 45, 35]
}
df = pd.DataFrame(data)
df['Attendance Percentage'] = (df['Classes_Attended'] / df['Total_Classes']) * 100

print("Students whose attendance is below 75%:\n", df[df['Attendance Percentage'] < 75])
