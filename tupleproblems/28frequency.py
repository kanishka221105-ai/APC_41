#28.	Count the frequency of each element in a tuple.
t=(1,2,1,3,2,1,4)
for i in set(t):
    print(i,":",t.count(i))
