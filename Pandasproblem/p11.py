# 11. Create a Pandas Series using a dictionary where patient IDs are the index and patient ages are the values.
# Perform:
# Find the average age. 
# Find the oldest patient. 
# Find the youngest patient. 
# Display patients above 60 years.[cite: 2]
import pandas as pd

patient_ages = {101: 55, 102: 68, 103: 42, 104: 75, 105: 61}
s = pd.Series(patient_ages)

print("Average age:", s.mean())
print("Oldest patient age:", s.max())
print("Youngest patient age:", s.min())
print("Patients above 60 years:\n", s[s > 60])