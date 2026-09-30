# 12. Create a Pandas Series using a dictionary containing student names and attendance percentages.
# Perform:
# Find the average attendance. 
# Display students with attendance below 75%. 
# Display students with attendance above 90%. 
# Find the highest attendance.
import pandas as pd

attendance_dict = {'Alice': 82.5, 'Bob': 70.0, 'Charlie': 95.0, 'Diana': 65.5, 'Ethan': 91.0}
s = pd.Series(attendance_dict)

print("Average attendance:", s.mean())
print("\nStudents with attendance below 75%:\n", s[s < 75])
print("\nStudents with attendance above 90%:\n", s[s > 90])
print("\nHighest attendance:", s.max())
