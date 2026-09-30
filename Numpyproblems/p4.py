# Create a NumPy array of integers from 1 to 20. Use Boolean indexing to separate and display the even and odd numbers.
import numpy as np
arr = np.arange(1, 21)
even_nums = arr[arr % 2 == 0]
odd_nums = arr[arr % 2 != 0]
print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
