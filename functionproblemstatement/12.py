#12.	Create a function that checks whether a given string or number is a palindrome.
def pal(str):
    rev=""
    for i in str:
        rev=i+rev
    if (str==rev):
        return "It is a palindrome."
    else:
        return "It is not a palindrome."
str=input("Enter a string:")
print(pal(str))
    