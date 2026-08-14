#13.	Accept 10 numbers and sort them in:
# •	Ascending order 
# •	Descending order
num=[]
for i in range(0,10):
    innum=int(input("Enter number:"))
    num.append(innum)
sorta=sorted(num)
sortb=sorta[::-1]
print("Ascending order:",sorta)
print("Descending order:",sortb)