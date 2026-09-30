# 8. Create a Pandas Series using a dictionary where the student names are keys and their marks are values.
# Perform:
# Display the Series. 
# Display marks of a particular student. 
# Find maximum and minimum marks. 
# Calculate the average marks. 
# Display students who scored more than 75. 
import pandas as pd

marks_dict = {'Alice': 85, 'Bob': 68, 'Charlie': 90, 'Diana': 72, 'Ethan': 78}
s = pd.Series(marks_dict)

print("Series:\n", s)
print("\nMarks of Alice:", s['Alice'])
print("Maximum marks:", s.max())
print("Minimum marks:", s.min())
print("Average marks:", s.mean())
print("\nStudents who scored more than 75:\n", s[s > 75])
