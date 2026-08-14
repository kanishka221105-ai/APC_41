#Reverse the given string without using built-in reverse functions. 
str=input("Enter a string:")
reverse=""
for ch in str:
    reverse=ch+reverse
print("Reversed string :",reverse)