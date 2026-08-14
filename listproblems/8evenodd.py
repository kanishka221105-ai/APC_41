#8.	Store 15 integers in a list. Count how many numbers are:
# •	Even 
# •	Odd
num=[2,4,9,8,60,54,34,23,69,2,6,9,1,5,9]
even=0
odd=0
for i in range(0,15):
    if num[i]%2==0:
        even+=1
    else:
        odd+=1
print("Even:",even)
print("Odd:",odd)