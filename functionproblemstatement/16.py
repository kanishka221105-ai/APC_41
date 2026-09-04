#16.	Create a function to find the second-largest number in a list.
def second_largest(lst):
    largest=second=lst[0]
    for i in lst:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i!=largest:
            second=i
    return second
lst=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    num=int(input("Enter element: "))
    lst.append(num)
print("Second largest element=",second_largest(lst))