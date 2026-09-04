#11.	Write a function that accepts a string and returns its reverse.
def rev(str):
    rev=""
    for i in str:
        rev=i+rev
    return rev
str=input("Enter a string:")
print("Reversed string:",rev(str))