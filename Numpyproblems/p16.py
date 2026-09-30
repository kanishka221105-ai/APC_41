# Store marks of 10 students in a NumPy array. Calculate:
# Highest marks 
# Lowest marks 
# Average marks 
# Median 
# Standard deviation
import numpy as np
marks = np.array([78, 85, 92, 63, 74, 90, 88, 79, 95, 82])
print("Highest marks:", marks.max())
print("Lowest marks:", marks.min())
print("Average marks:", marks.mean())
print("Median:", np.median(marks))
print("Standard deviation:", marks.std())