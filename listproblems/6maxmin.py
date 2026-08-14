#6.	Write a program to find the largest and smallest number in a list without using max() or min().
num=[4,7,5,2,8,9]
max=num[0]
min=num[0]
for i in range(0,len(num)):
    if num[i]>max:
        max=num[i]
    if num[i]<min:
        min=num[i]
print("Largest:",max)
print("Smallest:",min)

