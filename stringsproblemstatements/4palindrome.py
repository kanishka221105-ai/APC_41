#Check whether the entered string is a palindrome. 
str=input("Enter a string :")
reverse=""
for ch in str:
    reverse=ch+reverse
if(reverse==str):
    print("Yes it is a palindrome.")
else:
    print("Not a palindrome.")