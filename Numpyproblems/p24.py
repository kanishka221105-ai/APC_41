# Create a 3D array containing integers from 1 to 27. Flatten the array and calculate:
# Sum 
# Average 
# Maximum 
# Minimum
import numpy as np
arr = np.arange(1, 28).reshape(3, 3, 3)
flat_arr = arr.flatten()
print("Sum:", flat_arr.sum())
print("Average:", flat_arr.mean())
print("Maximum:", flat_arr.max())
print("Minimum:", flat_arr.min())