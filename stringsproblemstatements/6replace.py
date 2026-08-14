#Replace all occurrences of a given character with another character. 
str=input("Enter a string:")
old=input("Enter character to be replaced:")
new=input("Enter new character:")
result=""
for ch in str:
    if ch==old:
        ch=new
    result=result+ch
print(result)