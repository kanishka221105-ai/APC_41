#Remove all spaces from the input string. 
str=input("Enter a string:")
result=""
for ch in str:
    if ch==" ":
        ch=""
    result=result+ch
print("String without spaces:",result)