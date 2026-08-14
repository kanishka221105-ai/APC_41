# 7.	Accept 10 numbers from the user and store them in a list. Calculate:
# •	Sum 
# •	Average 
num=[]
for i in range(0,10):
    innum=int(input("Enter number:"))
    num.append(innum)
sum=sum(num)
avg=sum/len(num)
print("SUM=",sum)
print("AVERAGE=",avg)

