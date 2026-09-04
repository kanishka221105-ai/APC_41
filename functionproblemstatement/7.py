#7.	Write a function that accepts n and returns the sum of the first n natural numbers.
def sum(n):
    return (n*(n+1))/2
n=int(input("Enter a number:"))
print("Sum is:",sum(n))
