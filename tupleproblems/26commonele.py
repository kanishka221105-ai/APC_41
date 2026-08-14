#26.	Create two tuples and find the common elements between them.
t1=(1,2,3,4,5)
t2=(4,5,6,7)
print("Common:", tuple(set(t1)&set(t2)))
