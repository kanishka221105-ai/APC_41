#14.	Create a list containing duplicate values and display only unique elements.
num=[1,6,4,7,1,3,2,9,0,77,34,22,1,2,3]
new=[]
for i in num:
    if i not in new:
        new.append(i)
print("Original List:", num)
print("Updated Elements:", new)