#3.	Define a function that accepts two numbers and returns the greater number.
def great(a,b):
    if a>b:
        return a
    else:
        return b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
print("The greater number is:",great(a,b))
