#27.	Merge two tuples and remove duplicate elements.
t1=(1,2,3)
t2=(3,4,5)
merged=t1+t2
print(tuple(dict.fromkeys(merged)))
