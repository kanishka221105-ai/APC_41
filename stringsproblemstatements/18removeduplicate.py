#Remove duplicate characters while maintaining the original order. 
str=input("Enter a string:")
duplicate=""
for ch in str:
    if str.count(ch)>0 and ch not in duplicate:
        duplicate+=ch
print(duplicate)
