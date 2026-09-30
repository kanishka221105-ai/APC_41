# Create an array of 10 integers. Replace all elements greater than 50 with 0 using NumPy Boolean indexing.
import numpy as np
arr = np.array([12, 55, 34, 78, 23, 90, 45, 60, 11, 51])
arr[arr > 50] = 0
print("Modified array:", arr)
