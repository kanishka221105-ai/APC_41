#Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 
str=input("Enter a string: ")
vowels=0
consonants=0
digits=0
spaces=0
special=0
for ch in str:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1
print("No. of Vowels:", vowels)
print("No. of Consonants:", consonants)
print("No. of Digits:", digits)
print("No. of Spaces:", spaces)
print("No. of Special Characters:", special)