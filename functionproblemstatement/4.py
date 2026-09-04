#4.	Create a function simple_interest(p, r, t) to calculate simple interest.
def si(p,r,t):
    return (p*r*t)/100
p=float(input("Enter principal amount: "))
r=float(input("Enter rate of interest: "))
t=float(input("Enter time: "))
print("Simple Interest=",si(p,r,t))