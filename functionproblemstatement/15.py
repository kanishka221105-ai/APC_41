#15.	Write a function that accepts a list and returns a new list containing only unique elements.
def unique_elements(lst):
    unique=[]
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique
lst=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    num=int(input("Enter element: "))
    lst.append(num)
print("Unique elements=",unique_elements(lst))