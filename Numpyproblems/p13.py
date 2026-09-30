# Create an unsorted NumPy array and display it in:
# Ascending order 
# Descending order
import numpy as np
arr = np.array([34, 12, 56, 3, 23, 89, 45])
print("Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])