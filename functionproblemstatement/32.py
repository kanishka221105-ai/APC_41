#32.	Create separate functions for addition, subtraction, multiplication, and division. Pass these functions as arguments to another function called calculate().
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Division by zero not possible"
def calculate(func,a,b):
    return func(a,b)
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
print("Addition =",calculate(add,x,y))
print("Subtraction =",calculate(sub,x,y))
print("Multiplication =",calculate(mul,x,y))
print("Division =",calculate(div,x,y))