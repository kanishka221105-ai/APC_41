#36.	Use a lambda function to find the maximum of two numbers.
great=lambda a,b: a if a>b else b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("Greater:",great(a,b))