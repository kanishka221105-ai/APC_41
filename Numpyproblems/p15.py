# Create two NumPy arrays and concatenate them horizontally and vertically.
import numpy as np
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("Horizontal concatenation:\n", np.hstack((arr1, arr2)))
print("Vertical concatenation:\n", np.vstack((arr1, arr2)))