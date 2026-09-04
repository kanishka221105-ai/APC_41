#13.	Write a function that accepts a list of numbers and returns their average.
def avg(lst):
    total=0
    for i in lst:
        total+=i
    return total/len(lst)
lst=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    num=int(input("Enter element: "))
    lst.append(num)
print("Average=",avg(lst))