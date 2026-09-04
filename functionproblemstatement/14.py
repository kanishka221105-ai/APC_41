#14.	Define a function that accepts a list and an element and returns the number of times that element occurs.
def count_occur(lst,element):
    count=0
    for i in lst:
        if i==element:
            count+=1
    return count
lst=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    num=int(input("Enter element: "))
    lst.append(num)
ele=int(input("Enter element to search: "))
print("Occurrences=",count_occur(lst,ele))