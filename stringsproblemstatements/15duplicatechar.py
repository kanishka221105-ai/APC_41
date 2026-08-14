#Print all duplicate characters in a string. 
str=input("Enter a string:")
duplicate=""
for ch in str:
    if str.count(ch)>1 and ch not in duplicate:
        duplicate=duplicate+ch
print(duplicate)