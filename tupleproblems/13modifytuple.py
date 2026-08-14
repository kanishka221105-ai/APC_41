#13.	Modify a tuple by converting it into a list and then back into a tuple.
t=(1,2,3)
l=list(t)
l[1]=20
t=tuple(l)
print(t)
