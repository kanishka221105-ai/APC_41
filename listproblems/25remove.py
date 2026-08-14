#25.	Remove all duplicate elements while preserving the original order.
nums = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for item in nums:
    if item not in unique:
        unique.append(item)

print("Original List:", nums)
print("List after removing duplicates:", unique)