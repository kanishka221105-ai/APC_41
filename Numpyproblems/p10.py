# Create a 4 × 4 matrix and calculate the sum of each row and each column separately.
import numpy as np
mat = np.arange(1, 17).reshape(4, 4)
print("Row sums:", mat.sum(axis=1))
print("Column sums:", mat.sum(axis=0))