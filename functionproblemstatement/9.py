#9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
def largest_element(lst):
    largest=lst[0]
    for i in lst:
        if i>largest:
            largest=i
    return largest
lst=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    num=int(input("Enter element: "))
    lst.append(num)
print("Largest element=",largest_element(lst))