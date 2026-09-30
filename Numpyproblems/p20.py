# Create a (2, 3, 4) array and calculate:
# Sum of all elements 
# Sum of each layer 
# Sum along rows 
# Sum along columns
import numpy as np
arr = np.arange(1, 25).reshape(2, 3, 4)
print("Sum of all elements:", arr.sum())
print("Sum of each layer:\n", arr.sum(axis=(1, 2)))
print("Sum along rows:\n", arr.sum(axis=1))
print("Sum along columns:\n", arr.sum(axis=2))