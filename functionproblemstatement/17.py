#17.	Write a function that accepts n and returns the first n Fibonacci numbers.
def fibonacci(n):
    fib=[]
    a=0
    b=1
    for i in range(n):
        fib.append(a)
        c=a+b
        a=b
        b=c
    return fib
n=int(input("Enter value of n: "))
print("Fibonacci series=",fibonacci(n))