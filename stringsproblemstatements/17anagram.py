#Check whether two strings are anagrams. 
str1=input("Enter first string:").lower()
str2=input("Enter second string:").lower()
if sorted(str1)==sorted(str2):
    print("It is a anagram.")
else:
    print("Not a anagram.")
