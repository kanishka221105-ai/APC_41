#24.	Rotate a list:
# •	Left by one position 
# •	Right by one position
nums = [10, 20, 30, 40, 50]

# Left Rotation
left_rotate = nums[1:] + [nums[0]]

# Right Rotation
right_rotate = [nums[-1]] + nums[:-1]

print("Original List :", nums)
print("Left Rotation :", left_rotate)
print("Right Rotation:", right_rotate)