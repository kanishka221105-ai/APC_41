#12. Display all elements present at even index positions
num=[1,7,52,85,9,0,45,34]
print("Elements at even index positions:")
for i in range(0, len(num), 2):
    print(num[i], end=" ")