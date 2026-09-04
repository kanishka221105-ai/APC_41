#8.	Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(b,p):
    return b**p
b=int(input("Enter the base:"))
p=int(input("Enter the exponent:"))
print("Value is:",power(b,p))