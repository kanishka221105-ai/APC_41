# Create a random 3D NumPy array of shape (3, 4, 5). Flatten it and display only the elements that are:
# Greater than 50 
# Even numbers 
# Less than the average value
import numpy as np
arr = np.random.randint(1, 100, size=(3, 4, 5))
flat_arr = arr.flatten()
print("Elements greater than 50:", flat_arr[flat_arr > 50])
print("Even numbers:", flat_arr[flat_arr % 2 == 0])
print("Elements less than average:", flat_arr[flat_arr < flat_arr.mean()])