#17.	Find the largest and smallest number in a tuple without using max() and min().
t=(10,50,5,70,20)
largest=smallest=t[0]
for i in t:
    if i>largest: largest=i
    if i<smallest: smallest=i
print("Largest:", largest)
print("Smallest:", smallest)
