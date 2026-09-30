# Create a 4 × 4 NumPy array and write a program to:
# Display the first row 
# Display the last column 
# Display the diagonal elements 
# Display the elements from the second and third rows
import numpy as np
arr = np.arange(1, 17).reshape(4, 4)
print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Diagonal elements:", np.diagonal(arr))
print("Elements from second and third rows:\n", arr[1:3])